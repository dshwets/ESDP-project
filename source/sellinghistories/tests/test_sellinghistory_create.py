import json

from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect
from accounts.factories import UserFactory
from django.conf import settings
import redis

from products.models import Product
from products.factories import ProductFactory
from sellinghistories.models import SellingHistory


class SellingHistoryTestCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory(barcode=123456, qty=100)
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_sellinghistory')
        self.url = reverse('sellinghistory:add_product_in_cart')
        self.url_purchase = reverse('sellinghistory:create_sellinghistory')
        self.red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        self.red.flushall()

    def tearDown(self) -> None:
        self.client.logout()
        self.red.flushall()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def common_data(self):
        data = {
            'barcode': self.product.barcode,
            'qty': self.product.qty,
        }
        return data

    def test_unauthorized_get_add_product_in_cart(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_get_create_sellinghistory(self):
        self.assert_response_status(self.url_purchase, 'get', 302)

    def test_unauthorized_post_add_product_in_cart(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_unauthorized_post_create_sellinghistory(self):
        self.assert_response_status(self.url_purchase, 'post', 302)

    def test_authorized_without_permission_get_add_product_in_cart(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_get_create_sellinghistory(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url_purchase, 'post', 403)

    def test_authorized_without_permission_post_add_product_in_cart(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_add_product_in_cart(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('sellinghistory_create.html')
        self.assert_response_status(self.url, 'get', 200)

    def testauthorized_post_request_has_perm_add_product_in_cart(self):
        data = self.common_data()
        cart_name = f'cart:{self.user.pk}'
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertEqual(self.red.lrange(cart_name, 0, -1), [])
        response = self.client.post(self.url, data)
        self.assertEqual(self.red.llen(cart_name), 1)
        self.assertEqual(
            json.loads(self.red.lrange(cart_name, 0, -1)[0])['product_pk'],
            self.product.pk
        )
        self.assertEqual(
            json.loads(self.red.lrange(cart_name, 0, -1)[0])['qty'],
            self.product.qty
        )
        self.client.get(self.url_purchase)
        self.assertEqual(self.red.lrange(cart_name, 0, -1), [])
        self.assertEqual(Product.objects.get(pk=self.product.pk).qty, 0)
        self.assertTrue(SellingHistory.objects.all().exists())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, self.url)

