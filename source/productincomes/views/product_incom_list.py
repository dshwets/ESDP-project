from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from productincomes.models import ProductIncomes


class ProductIncomesListView(PermissionRequiredMixin, ListView):
    template_name = 'product_incom_list.html'
    queryset = ProductIncomes.objects.order_by('-pk')
    context_object_name = 'product_incoms'
    permission_required = 'product_incoms:can_view_product_incomes'
    paginate_by = 30
    paginate_orphans = 4