from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from hostelservices.models import HostelService, SellingPrice, PurchasePrice


class HostelServiceCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.hostelservice = HostelServiceFactory()
        self.sellingprice = SellingPriceFactory(hostel_service=self.hostelservice)
        self.purchaseprice = PurchasePriceFactory(hostel_service=self.hostelservice)
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_hostelservice')
        self.url = reverse('hostelservices:hostelservices_add')

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        data = {
            'service_name-service_name': 'TestSERVICE',
            'selling_price-selling_price': 800.00,
            'purchase_price-purchase_price': 700.00,
        }
        return data

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_unauthorized_get_create_hostelservices(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_create_hostelservice(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_create_hostelservice(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_get_request_has_perm_create_hostelservice(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('hostelservices_create.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_without_permission_post_create_hostelservice(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_create_hostelservice(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('hostelservices:hostelservices_list')
        self.assertEqual(response.url, redirect_url)

    def test_authorized_with_permission_post_create_hostelservice_with_empty_service_nama(self):
        data = data = {
            'service_name-service_name': '',
            'selling_price-selling_price': 800.00,
            'purchase_price-purchase_price': 700.00,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'service_name-service_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_hostelservice_with_empty_selling_price(self):
        data = data = {
            'service_name-service_name': 'TestTest',
            'selling_price-selling_price': '',
            'purchase_price-purchase_price': 700.00,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'selling_price-selling_price'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')



