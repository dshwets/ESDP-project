from django.contrib.auth.mixins import  PermissionRequiredMixin
from django.views.generic import ListView

from products.models import Product


class ProductListView(PermissionRequiredMixin, ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    permission_required = 'products.can_view_product'
    paginate_by = 20
    paginate_orphans = 4
    ordering = ['title']