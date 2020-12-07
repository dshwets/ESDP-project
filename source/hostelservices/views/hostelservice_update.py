from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
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
        selling_price = SellingPrice.objects.filter(hostel_service=self.object).last()
        purchase_price = PurchasePrice.objects.filter(hostel_service=self.object).last()
        kwargs.update(instance={
            'service_name': self.object,
            'selling_price': selling_price,
            'purchase_price': purchase_price,
        })
        return kwargs

    def form_valid(self, form):
        service_name = form.cleaned_data['service_name']['service_name']
        purchase_price = form.cleaned_data['purchase_price']['purchase_price']
        selling_price = form.cleaned_data['selling_price']['selling_price']
        self.object.service_name = service_name
        old_p_price = PurchasePrice.objects.filter(hostel_service=self.object).last()
        old_s_price = SellingPrice.objects.filter(hostel_service=self.object).last()
        if old_p_price.purchase_price != purchase_price:
            PurchasePrice.objects.create(hostel_service=self.object, purchase_price=purchase_price)
        if old_s_price.selling_price != selling_price:
            SellingPrice.objects.create(hostel_service=self.object, selling_price=selling_price)
        self.object.save()
        return redirect(self.get_success_url())