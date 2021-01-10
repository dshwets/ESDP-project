from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from employees.factories import EmployeeFactory
from employees.models import Employee


class EmployeeCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.employee = EmployeeFactory()
        self.user = UserFactory(username='some_admin')
        self.permission_add = Permission.objects.get(codename='can_add_employee')
        self.url = reverse('employees:employee_create')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_employee(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_authorized_without_permission_get_create_employee(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_get_request_has_perm_create_employee(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('product_create.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_unauthorized_post_create_employee(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_post_create_employee(self):
        data = {
            'first_name': 'test_name',
            'last_name': 'test_name',
            'passport_id': 10,
            'phone_number': '+12125552368',
            'relative_phone_number': '+12125552368',
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_post_request_has_perm_create_employee(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        data = {
            'first_name': 'first_name',
            'last_name': 'test_name',
            'passport_id': "11222111",
            'phone_number': '+996500500500',
            'relative_phone_number': '+996500500501',
            'address': '+150 Ahunbaeva street, 79',
            'note': '+12125552368',
            'deposit_amount': 500
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Employee.objects.filter(first_name='first_name').exists())

    def test_authorized_with_permission_post_create_employee_with_empty_name(self):
        data = {
            'first_name': '',
            'last_name': 'test_name',
            'passport_id': "11222111",
            'phone_number': '+996500500500',
            'relative_phone_number': '+996500500501',
            'address': '+150 Ahunbaeva street, 79',
            'note': '+12125552368',
            'deposit_amount': 500
        }
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'first_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)
