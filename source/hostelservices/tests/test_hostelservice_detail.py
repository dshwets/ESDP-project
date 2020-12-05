from django.contrib.auth.models import Permission
from accounts.factories import UserFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse


class HostelServiceDetailViewTestCase(TestCase):

    def setUp(self):
        self.permission = Permission.objects.get(codename='can_view_hostelservice')
        self.service = HostelServiceFactory()
        self.purchase_price = PurchasePriceFactory(
            hostel_service=self.service,
            purchase_price='50'
        )
        self.selling_price = SellingPriceFactory(
            hostel_service=self.service,
            selling_price='50'
        )
        self.user = UserFactory(username='some_admin')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_hostelservices_detail(self):
        url = reverse('hostelservices:hostelservices_detail', kwargs={'pk': self.service.pk})
        response = self.client.get(url)
        redirect_url = reverse('accounts:login') + '?next=' + url
        self.check_redirect(response, redirect_url)

    def test_authorized_without_permission_get_hostelservices_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:detail_view', args=(self.service.pk,)), follow=True)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_get_hostelservices_detail(self):
        self.client.login(username='some_admin', password='pass')
        self.user.user_permissions.add(self.permission)
        response = self.client.get(reverse('hostelguests:detail_view', args=(self.service.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hostelservice_detail.html')