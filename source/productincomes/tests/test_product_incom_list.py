from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from productincomes.factories import ProductIncomesFactory


class ProductIncomesListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.p_i = ProductIncomesFactory(
        )
        self.user = UserFactory(username='some_admin')
        self.url = reverse('product_incom:list_product_incom')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_product_incom_list(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_authorized_without_permission_get_product_incom_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)


