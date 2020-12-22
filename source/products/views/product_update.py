from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from products.forms import ProductForm
from products.models import Product


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    permission_required = 'products.can_change_product'

    def get_success_url(self):
        return reverse('products:product_list')