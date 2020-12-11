from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from hostelservices.forms import HostelServiceMultiForm
from hostelservices.models import HostelService, SellingPrice, PurchasePrice


class HostelServiceCreateView(PermissionRequiredMixin, CreateView):
    model = HostelService
    form_class = HostelServiceMultiForm
    template_name = 'hostelservices_create.html'
    permission_required = 'hostelservices.can_add_hostelservice'
    success_url = reverse_lazy('hostelservices:hostelservices_list')

    def form_valid(self, form):
        hostelservice = form.save(commit=False)
        hostelservice.service_name = form.cleaned_data['service_name']
        hostelservice['service_name'].save()
        hostel_service_object = HostelService.objects.last()
        SellingPrice.objects.create(hostel_service=hostel_service_object, selling_price=form.cleaned_data['selling_price']['selling_price'])
        PurchasePrice.objects.create(hostel_service=hostel_service_object, purchase_price=form.cleaned_data['purchase_price']['purchase_price'])
        return redirect('hostelservices:hostelservices_detail', pk=hostel_service_object.pk)