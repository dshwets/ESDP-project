from django.contrib.auth.models import Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from aboutguests.factories import GuestFactory
from welcomeguests.factories import WelcomeGuestFactory


class WelcomeGuestCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.welcomeguest = WelcomeGuestFactory(guest=GuestFactory())
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_welcomeguest')
        self.guest = GuestFactory(photo=SimpleUploadedFile('test.jpg', content=b'', content_type='image/jpg'))

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_welcomeguest(self):
        self.assert_response_status(reverse('hostelguests:welcomeguest_create', args=(self.welcomeguest.id,)), 'get', 302)

    def test_unauthorized_post_create_welcomeguest(self):
        self.assert_response_status(reverse('hostelguests:welcomeguest_create', args=(self.welcomeguest.id,)), 'post',
                                    302)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_authorized_without_permission_get_create_welcomeguest(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:welcomeguest_create', args=(self.welcomeguest.id,)), 'get', 403)

    def test_authorized_without_permission_post_create_welcomeguest(self):
        url = reverse('hostelguests:welcomeguest_create', args=(self.welcomeguest.id,))
        data = {
            'description': self.welcomeguest.description,
            'guest': self.welcomeguest.guest
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_create_welcomeguest(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('welcomeguest_create.html')
        self.assert_response_status(reverse('hostelguests:welcomeguest_create', args=(self.welcomeguest.id,)), 'get', 200)

    def testauthorized_post_request_has_perm_create_welcomeguest(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:welcomeguest_create', args=(self.guest.pk,)), 'post', 302)


    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)