from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from products.forms import ProductForm
from products.models import Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    model = Product
    permission_required = 'products.can_add_product'

    def get_success_url(self):
        return reverse('products:product_list')

    def get_form_kwargs(self):
        kwargs = super(ProductCreateView, self).get_form_kwargs()
        kwargs['created_by'] = self.request.user.pk
        return kwargs