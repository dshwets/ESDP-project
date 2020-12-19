from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView

from products.models import Product


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product_delete.html'
    model = Product
    permission_required = 'product.can_delete_product'

    def get_success_url(self):
        return reverse('products:product_list')

    # TODO Надо написать логику чтобы пользователь не мог удалить товар с которым были уже операции