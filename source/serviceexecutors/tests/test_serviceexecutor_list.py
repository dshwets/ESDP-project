from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from serviceexecutors.factories import ServiceExecutorFactory



class ServiceExecutorListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_service_executor_list(self):
        response = self.client.get(reverse('serviceexecutors:serviceexecutors_list'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('serviceexecutors:serviceexecutors_list')
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_authorized_get_service_executor_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('serviceexecutors:serviceexecutors_list'))
        self.assertEqual(response.status_code, 200)