from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from sellinghistories.factories import SellingHistoryFactory
from products.models import Product
from sellinghistories.models import SellingHistory


class ProductDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.sellinghistory = SellingHistoryFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_sellinghistory')
        self.permission_view = Permission.objects.get(codename='can_view_sellinghistory')
        self.url = reverse('sellinghistory:sellinghistory_delete', kwargs={'pk': self.sellinghistory.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_sellinghistory_delete_unauthorized_get_request(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_sellinghistory_delete_unauthorized_post_request(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_sellinghistory_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'get', 403)

    def test_sellinghistory_delete_authorized_post_request_has_perm_product_not_found(self):
        self.user.user_permissions.add(self.permission_view)
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        fake_id = self.sellinghistory.id+25
        self.assert_response_status(reverse('sellinghistory:sellinghistory_delete', args=(fake_id,)), 'get', 404)

    def test_authorized_request_has_perm_delete_sellinghistory(self):
        self.user.user_permissions.add(self.permission)
        self.user.user_permissions.add(self.permission_view)
        self.client.login(username='some_admin', password='pass')
        redirect_url = reverse('sellinghistory:list_sellinghistory')
        product = self.sellinghistory.product
        product.qty = self.sellinghistory.qty
        product.save()
        response = self.client.post(self.url)
        self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertEqual(self.sellinghistory.qty * 2, Product.objects.first().qty)
        self.assertFalse(SellingHistory.objects.all().exists())
