from django.contrib.auth.models import Permission
from accounts.factories import UserFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from products.factories import ProductFactory


class HostelServiceDetailViewTestCase(TestCase):

    def setUp(self):
        self.permission = Permission.objects.get(codename='can_view_product')
        self.product = ProductFactory()
        self.user = UserFactory(username='some_admin')
        self.url = reverse('api:barcode_product', kwargs={'barcode':self.product.barcode})

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_product_barcode(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_authorized_without_permission_get_product_barcode(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_get_product_barcode(self):
        self.client.login(username='some_admin', password='pass')
        self.user.user_permissions.add(self.permission)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_authorized_with_permission_get_new_product_barcode(self):
        self.client.login(username='some_admin', password='pass')
        self.user.user_permissions.add(self.permission)
        barcode = 123123
        url = reverse('api:barcode_product', kwargs={'barcode':barcode})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['barcode'], barcode)