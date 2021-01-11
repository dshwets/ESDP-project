from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from productincomes.models import Incomes, ProductIncomes


class ProductIncomesDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'productincomes_detail.html'
    model = Incomes
    permission_required = 'productincomes.can_view_incomes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = ProductIncomes.objects.filter(incomes=self.object)
        context['products'] = ProductIncomes.objects.filter(incomes=self.object)
        return context

