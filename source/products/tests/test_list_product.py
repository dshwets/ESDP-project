from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from products.factories import ProductFactory


class ProductListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product = ProductFactory()
        self.user = UserFactory(username='some_admin')
        self.permission_add = Permission.objects.get(codename='can_view_product')
        self.url = reverse('products:product_list')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_product_list(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_authorized_without_permission_get_product_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_product_list(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('product_list.html')
        self.assert_response_status(self.url, 'get', 200)

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)