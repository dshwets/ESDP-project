from django.contrib.auth.models import Permission
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from django.http import HttpResponseRedirect, response, request
from django.test import TestCase, Client
from django.urls import reverse


class GuestDetailViewTestCase(TestCase):

    def setUp(self):
        self.guest = GuestFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_view_guest')

    def tearDown(self) -> None:
        self.guest.delete()
        self.user.delete()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_guest_daetail_logouted_request(self):
        rever = reverse('hostelguests:detail_view', kwargs={'pk':self.guest.pk})
        response = self.client.get(rever)
        redirect_url = reverse('accounts:login') + '?next=' + rever
        self.check_redirect(response, redirect_url)

    def test_detail_template(self):
        '''Make sure the `<int:pk>/guestdetail.html` template is used'''
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:detail_view', args=(self.guest.id,)), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'guestdetail.html')
