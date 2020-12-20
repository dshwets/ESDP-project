from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from products.factories import ProductFactory
from products.models import Product


class ProductCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory()
        self.user = UserFactory(username='some_admin')
        self.permission_add = Permission.objects.get(codename='can_add_product')
        self.url = reverse('products:product_create')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_product(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_create_product(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_create_product(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_create_product(self):
        data = {
            'title': 'test_name',
            'qty': 10,
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_create_product(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('product_create.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_post_request_has_perm_create_product(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        data = {
            'title': 'test_name',
            'qty': 10,
        }
        response = self.client.post(self.url, data)
        self.assertTrue(Product.objects.filter(title='test_name').exists())

    def test_authorized_with_permission_post_create_product_with_empty_name(self):
        data = {
            'title': '',
            'qty': 10,
        }
        self.user.user_permissions.add(self.permission_add)
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
