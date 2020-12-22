from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from products.factories import ProductFactory
from products.models import Product


class ProductUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_product')
        self.url = reverse('products:product_update', kwargs={'pk': self.product.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        data = {
            'title': 'TestTitle',
            'qty': 100,
            'barcode': 1111111,
            'selling_price': 100.50,
        }
        return data

    def test_unauthorized_get_update_product(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_product(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_product(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_update_product(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_update_update(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('product_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_with_permission_post_update_product(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(product.title, data['title'])
        self.assertEqual(product.qty, data['qty'])
        self.assertEqual(product.barcode, data['barcode'])
        self.assertEqual(product.selling_price, data['selling_price'])
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('products:product_list')
        self.assertEqual(response.url, redirect_url)

    def test_authorized_with_permission_post_update_product_with_empty_title(self):
        data = {
            'title': '',
            'qty': 100,
            'barcode': 1111111,
            'selling_price': 100.50,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'title'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)