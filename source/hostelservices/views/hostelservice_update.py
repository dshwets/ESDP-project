from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from hostelservices.forms import HostelServiceMultiForm
from hostelservices.models import HostelService, SellingPrice, PurchasePrice


class HostelServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = HostelService
    template_name = 'hostelservice_form.html'
    form_class = HostelServiceMultiForm
    permission_required = 'hostelservices.can_change_hostelservice'
    success_url = reverse_lazy('hostelservices:hostelservices_list')

    def get_form_kwargs(self):
        kwargs = super(HostelServiceUpdateView, self).get_form_kwargs()
        self.object = kwargs['instance']
        selling_price = SellingPrice.objects.get(hostel_service=self.object)
        purchase_price = PurchasePrice.objects.get(hostel_service=self.object)
        kwargs.update(instance={
            'service_name': self.object,
            'selling_price': selling_price,
            'purchase_price': purchase_price,
        })
        return kwargs
