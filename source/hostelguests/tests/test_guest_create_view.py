from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse


class GuestCreateTestCase(TestCase):
    def test_open_create_article(self):
        response = self.client.get(reverse('hostelguests:guest_create'))
        redirect_url = reverse('accounts:login')+ '?next=' + reverse('hostelguests:guest_create')
        self.check_redirect(response, redirect_url)