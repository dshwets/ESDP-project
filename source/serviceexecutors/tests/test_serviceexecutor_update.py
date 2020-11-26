from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from serviceexecutors.factories import ServiceExecutorFactory


class ServiceExecutorUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_serviceexecutor')
        self.url = reverse('serviceexecutors:serviceexecutor_update', kwargs={'pk': self.serviceexecutor.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        data = {
            'name': 'TestName',
            'last_name': 'TestLastName',
            'middle_name': 'TestMiddleName',
        }
        return data

    def test_unauthorized_get_update_serviceexecutor(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_serviceexecutor(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_serviceexecutor(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_update_serviceexecutor(self):
        data =  self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_update_serviceexecutor(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('serviceexecutor_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_with_permission_post_update_serviceexecutor(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        print(self.user.user_permissions.all())
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
    #     self.assertEqual(type(response), HttpResponseRedirect)
    #     redirect_url = reverse('hostelguests:detail_view',kwargs={'pk':self.guest.pk})
    #     self.assertEqual(response.url, redirect_url)
    #     guest = Guest.objects.get(pk=self.guest.pk)
    #     self.assertEqual(guest.first_name, data['first_name'])
    #     self.assertEqual(guest.last_name, data['last_name'])
    #     self.assertEqual(guest.middle_name, data['middle_name'])
    #     self.assertEqual(guest.birth_country, data['birth_country'])
    #     self.assertEqual(guest.passport_id, data['passport_id'])
    #     self.assertEqual(guest.document_maker, data['document_maker'])
    #     self.assertTrue(guest.photo)
    #
    #
    # def test_authorized_post_request_has_perm_update_serviceexecutor(self):
    #     self.user.user_permissions.add(self.permission)
    #     self.client.login(username='some_admin', password='pass')
    #     data = {
    #         'name': self.serviceexecutor.name,
    #         'last_name': self.serviceexecutor.last_name,
    #         'middle_name': self.serviceexecutor.middle_name,
    #     }
    #     redirect_url = reverse('hostelguests:guest_list')
    #     response = self.client.post(self.url, data)
    #     print(response)
    #     self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
    #                          target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    # def test_authorized_with_permission_post_create_serviceexecutor_with_empty_name(self):
    #     url = reverse('serviceexecutors:serviceexecutor_create')
    #     data = data = {
    #         'name': '',
    #         'last_name': self.serviceexecutor.last_name,
    #         'middle_name': self.serviceexecutor.middle_name,
    #     }
    #     self.user.user_permissions.add(self.permission)
    #     self.client.login(username='some_admin', password='pass')
    #     response = self.client.post(url, data)
    #     field = 'name'
    #     self.assertFormError(response, 'form', field, 'Обязательное поле.')
    #
    # def assert_response_status(self, url, method, code):
    #     if method == "get":
    #         response = self.client.get(url)
    #         self.assertEqual(response.status_code, code)
    #     elif method == "post":
    #         response = self.client.post(url)
    #         self.assertEqual(response.status_code, code)
    #
    # def test_authorized_with_permission_post_update_guest(self):
    #     url = reverse('hostelguests:guest_update', kwargs={'pk':self.guest.pk})
    #     data = self.common_data()
    #     self.user.user_permissions.add(self.permission)
    #     self.client.login(username='some_admin', password='pass')
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(type(response), HttpResponseRedirect)
    #     redirect_url = reverse('hostelguests:detail_view',kwargs={'pk':self.guest.pk})
    #     self.assertEqual(response.url, redirect_url)
    #     guest = Guest.objects.get(pk=self.guest.pk)
    #     self.assertEqual(guest.first_name, data['first_name'])
    #     self.assertEqual(guest.last_name, data['last_name'])
    #     self.assertEqual(guest.middle_name, data['middle_name'])
    #     self.assertEqual(guest.birth_country, data['birth_country'])
    #     self.assertEqual(guest.passport_id, data['passport_id'])
    #     self.assertEqual(guest.document_maker, data['document_maker'])
    #     self.assertTrue(guest.photo)

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)