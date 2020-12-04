from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import DetailView

from hostelservices.models import HostelService


class HostelServiceDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'hostelservice_detail.html'
    model = HostelService
    permission_required = 'hostelservice.can_view_hostelservice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selling_price, purchase_price = self.paginate_price(self.object)
        context['selling_price'] = selling_price
        context['purchase_price'] = purchase_price
        return context

    def paginate_price(self, hostelservice):
        selling_price = hostelservice.selling_price.all().order_by('-pk')[0]
        purchase_price = hostelservice.purchase_price.all().order_by('-pk')[0]
        return selling_price, purchase_price