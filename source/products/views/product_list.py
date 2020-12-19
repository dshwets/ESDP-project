from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from products.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 20
    paginate_orphans = 4
    ordering = ['title']