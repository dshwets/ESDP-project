from django.contrib.auth.models import Permission
from django.urls import reverse
from rest_framework.test import APITestCase

from accounts.factories import UserFactory
from productincomes.models import Incomes, ProductIncomes
from products.models import Product
from serviceexecutors.factories import ServiceExecutorFactory


class ProductIncomesCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_incomes')
        self.permission_2 = Permission.objects.get(codename='can_view_product')
        self.url = reverse('api:product_incoming_create')

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        data = {
             "serviceexecutor": f'{self.serviceexecutor.last_name} {self.serviceexecutor.name}',
             "title-1": "Test1",
             "barcode-1": "12345",
             "qty-1": "22",
             "purchase-price-1": "11"
        }

        return data

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_unauthorized_get_create_product_incomes(self):
        self.assert_response_status(self.url, 'get', 403)

    def test_unauthorized_post_create_product_incomes(self):
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_get_create_product_incomes(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_get_request_has_perm_create_product_incomes(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('product_incom_create.html')
        self.assert_response_status(self.url, 'get', 405)

    def test_authorized_without_permission_post_create_product_incomes(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_create_product_incomes(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.user.user_permissions.add(self.permission_2)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        new_product = Product.objects.get(barcode=data['barcode-1'])
        self.assertEqual(new_product.title, data['title-1'])
        new_incomes = Incomes.objects.first()
        self.assertEqual(new_incomes.services_executor, self.serviceexecutor)
        new_product_incomes = ProductIncomes.objects.first()
        self.assertEqual(new_product_incomes.product, new_product)

    def test_authorized_with_permission_post_product_incomes_with_empty_service_executor(self):
        data = {
             "serviceexecutor": '',
             "title-1": "Test1",
             "barcode-1": "12345",
             "qty-1": "22",
             "purchase-price-1": "11"
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Заполните все поля')
