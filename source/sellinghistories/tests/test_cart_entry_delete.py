from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from django.conf import settings
import redis

from products.factories import ProductFactory


class DeleteItemFromCartTestCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory(barcode=123456, qty=100)
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_sellinghistory')
        self.permission_add_to_cart = Permission.objects.get(codename='can_add_sellinghistory')
        self.url = reverse('sellinghistory:remove_product_from_cart', args=[0])
        self.url_add = reverse('sellinghistory:add_product_in_cart')
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

    def test_unauthorized_get_remove_cart_entry(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_remove_cart_entry(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_remove_cart_entry(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'get', 403)

    def test_authorized_without_permission_post_remove_cart_entry(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_remove_cart_entry(self):
        data = self.common_data()
        cart_name = f'cart:{self.user.pk}'
        self.user.user_permissions.add(self.permission_add_to_cart)
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('sellinghistory_create.html')
        self.assert_response_status(self.url_add, 'get', 200)
        self.assertEqual(self.red.lrange(cart_name, 0, -1), [])
        self.client.post(self.url_add, data)
        self.assertEqual(self.red.llen(cart_name), 1)
        self.client.get(reverse('sellinghistory:remove_product_from_cart', kwargs={'pk': 0}))
        self.assertEqual(self.red.llen(cart_name), 0)
