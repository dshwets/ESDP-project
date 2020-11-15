from django.contrib.auth.models import Permission
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse


class GuestDetailViewTestCase(TestCase):

    def setUp(self):
        self.guest = GuestFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_view_guest')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_guest_detail(self):
        rever = reverse('hostelguests:detail_view', kwargs={'pk':self.guest.pk})
        response = self.client.get(rever)
        redirect_url = reverse('accounts:login') + '?next=' + rever
        self.check_redirect(response, redirect_url)

    def test_authorized_with_permission_get_guest_detail(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:detail_view', args=(self.guest.id,)), follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'guestdetail.html')

    def test_authorized_without_permission_get_guest_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:detail_view', args=(self.guest.id,)), follow=True)
        self.assertEqual(response.status_code,403)
