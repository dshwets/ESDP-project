from accounts.factories import UserFactory
from accounts.models import User
from hostelguests.factories import GuestFactory
from journalservices.models import JournalService
from hostelservices.factories import HostelServiceFactory, SellingPriceFactory, PurchasePriceFactory
from django.test import TestCase
from django.urls import reverse


class ServiceExecutorDetailViewTestCase(TestCase):

    def setUp(self):
        self.guest = GuestFactory()
        self.hostelservice = HostelServiceFactory()
        self.selling_price = SellingPriceFactory(hostel_service=self.hostelservice)
        self.purchase_price = PurchasePriceFactory(hostel_service=self.hostelservice)
        self.journalservice = JournalService.objects.create(
            guest=self.guest, hostel_service=self.hostelservice,
            purchase_price=self.purchase_price, selling_price=self.selling_price)
        self.user = User.objects.create_superuser(username='admin', email='admin@admin.com', password='admin')
        self.user_2 = UserFactory(username='some_admin', password='pass')

    def tearDown(self):
        self.client.logout()

    def test_unauthorized_get_serviceexecutor_detail(self):
        url = reverse('journalservices:journal_detail', kwargs={'pk': self.journalservice.pk})
        response = self.client.get(url)
        redirect_url = reverse('accounts:login') + '?next=' + url
        self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_authorized_has_permissions_get_serviceexecutor_detail(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('journalservices:journal_detail', args=(self.journalservice.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'journalservice_detail.html')

    def test_authorized_without_permission_get_serviceexecutor_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('journalservices:journal_detail', args=(self.journalservice.pk,)))
        self.assertEqual(response.status_code, 403)