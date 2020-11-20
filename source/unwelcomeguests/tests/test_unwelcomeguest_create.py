# страницу открывает неавторизованный пользователь
# страницу открывает авторизованный пользователь без прав доступа
# # страницу открывает авторизованный пользователь с правами доступа
# на открытие страницы не авторизованным пользователем приходит статус ответа 302
# на открытие страницы авторизованным пользователем без прав доступа приходит ошибка 403
# на открытие страницы авторизованным пользователем с правами доступа приходит статус 200. После заполнения полей и отправки запроса POST 302 статус
from django.contrib.auth.models import Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from aboutguests.factories import GuestFactory
from unwelcomeguests.factories import UnwelcomeGuestFactory


class UnWelcomeGuestCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.unwelcomeguest = UnwelcomeGuestFactory(guest=GuestFactory())
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_unwelcomeguest')
        self.guest = GuestFactory(photo=SimpleUploadedFile('test.jpg', content=b'', content_type='image/jpg'))

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_unwelcomeguest(self):
        self.assert_response_status(reverse('hostelguests:unwelcomeguest_create', kwargs={'pk': self.unwelcomeguest.pk}), 'get', 302)

    def test_unauthorized_post_create_unwelcomeguest(self):
        self.assert_response_status(reverse('hostelguests:unwelcomeguest_create', kwargs={'pk': self.unwelcomeguest.pk}), 'post',
                                    302)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_authorized_without_permission_get_create_unwelcomeguest(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:unwelcomeguest_create', kwargs={'pk': self.unwelcomeguest.pk}), 'get', 403)

    def test_authorized_without_permission_post_create_unwelcomeguest(self):
        url = reverse('hostelguests:welcomeguest_create', kwargs={'pk': self.unwelcomeguest.pk})
        data = {
            'description': self.unwelcomeguest.description,
            'guest': self.unwelcomeguest.guest
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_create_unwelcomeguest(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('unwelcomeguest_create.html')
        self.assert_response_status(reverse('hostelguests:unwelcomeguest_create', kwargs={'pk': self.unwelcomeguest.pk}), 'get', 200)

    def testauthorized_post_request_has_perm_create_unwelcomeguest(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:unwelcomeguest_create', kwargs={'pk': self.unwelcomeguest.pk}), 'post', 302)

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

