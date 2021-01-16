from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from sellinghistories.factories import SellingHistoryFactory
from sellinghistories.models import SellingHistory


class SellingHistoryUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.sel_his = SellingHistoryFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_sellinghistory')
        self.url = reverse('sellinghistory:sellinghistory_update', kwargs={'pk': self.sel_his.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def data(self):
        data = {
            'qty': 100,
            'selling_price': 100.50,
        }
        return data

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_unauthorized_get_update_sel_his(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_sel_his(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_sel_his(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_get_request_has_perm_update_sel_his(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('selling_history_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_without_permission_post_update_sel_his(self):
        data = self.data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_update_sel_his(self):
        data = self.data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)

    def test_authorized_with_permission_post_update_sel_his_with_empty_last_name(self):
        data = {
            'qty': "",
            'selling_price': 100.50,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'qty'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')