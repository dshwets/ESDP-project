from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from hostelservices.forms import HostelServiceMultiForm
from hostelservices.models import HostelService
from serviceexecutors.forms import ServiceExecutorForm
from serviceexecutors.models import ServiceExecutor


class HostelServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = HostelService
    form_class = HostelServiceMultiForm
    permission_required = 'serviceexecutors.can_change_serviceexecutor'
    success_url = reverse_lazy('hostelservices:hostelservices_list')

    def get_form_kwargs(self):
        kwargs = super(HostelServiceUpdateView, self).get_form_kwargs()
        print(kwargs['instance'])
        kwargs.update(instance={
            'service_name': self.object,
            'selling_price': self.object.selling_price,
            'purchase_price': self.object.purchase_price,
        })
        return kwargs

# class HostelServiceUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = 'serviceexecutor_update.html'
#     form_class = ServiceExecutorForm
#     model = ServiceExecutor
#     permission_required = 'serviceexecutors.can_change_serviceexecutor'
#
#     def get(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         sellingprice_form = SellingPriceFormSet()
#         purchaseprice_form = PurchasePriceFormSet()
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   sellingprice_form=sellingprice_form,
#                                   purchaseprice_form=purchaseprice_form)
#         )
#
#
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         sellingprice_form = SellingPriceFormSet(self.request.POST)
#         purchaseprice_form = PurchasePriceFormSet(self.request.POST)
#         if (form.is_valid() and sellingprice_form.is_valid() and purchaseprice_form.is_valid()):
#             return self.form_valid(form, sellingprice_form, purchaseprice_form)
#         else:
#             self.form_invalid(form, sellingprice_form, purchaseprice_form)
#
#     def form_valid(self, form, sellingprice_form, purchaseprice_form):
#         self.object = form.save()
#         sellingprice_form = self.object
#         purchaseprice_form = self.object
#         return HttpResponseRedirect(self.get_success_url())
#
#     def form_invalid(self, form, sellingprice_form, purchaseprice_form):
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   sellingprice_form=sellingprice_form,
#                                   purchaseprice_form=purchaseprice_form))
#
#     def get_success_url(self):
#         return reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.object.pk})
