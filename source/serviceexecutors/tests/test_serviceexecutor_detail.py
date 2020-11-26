from django.contrib.auth.models import Permission
from accounts.factories import UserFactory
from serviceexecutors.factories import ServiceExecutorFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse


class ServiceExecutorDetailViewTestCase(TestCase):

    def setUp(self):
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_view_serviceexecutor')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_serviceexecutor_detail(self):
        url = reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.serviceexecutor.pk})
        response = self.client.get(url)
        redirect_url = reverse('accounts:login') + '?next=' + url
        self.check_redirect(response, redirect_url)

    def test_authorized_with_permission_get_serviceexecutor_detail(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('serviceexecutors:serviceexecutor_view', args=(self.serviceexecutor.id,)), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'serviceexecutor_detail.html')

    def test_authorized_without_permission_get_serviceexecutor_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('serviceexecutors:serviceexecutor_view', args=(self.serviceexecutor.id,)), follow=True)
        self.assertEqual(response.status_code,403)