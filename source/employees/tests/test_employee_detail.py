from django.contrib.auth.models import Permission
from employees.factories import EmployeeFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory

class EmployeeDetailTestCase(TestCase):

    def setUp(self):
        self.employee = EmployeeFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_view_employee')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_employee_detail(self):
        url = reverse('employees:employee_detail', kwargs={'pk': self.employee.pk})
        response = self.client.get(url)
        redirect_url = reverse('accounts:login') + '?next=' + url
        self.check_redirect(response, redirect_url)

    def test_authorized_with_permission_get_employee_detail(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('employees:employee_detail', args=(self.employee.id,)), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'employee_detail.html')

    def test_authorized_without_permission_get_employee_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('employees:employee_detail', args=(self.employee.id,)), follow=True)
        self.assertEqual(response.status_code,403)
