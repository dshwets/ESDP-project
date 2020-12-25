from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from productincomes.models import ProductIncomes


class ProductIncomesListView(LoginRequiredMixin, ListView):
    template_name = 'product_incom_list.html'
    queryset = ProductIncomes.objects.order_by('-pk')
    context_object_name = 'product_incoms'
    paginate_by = 30
    paginate_orphans = 4