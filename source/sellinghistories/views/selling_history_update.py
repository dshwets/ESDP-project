from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from sellinghistories.forms import SellingHistoryForm
from sellinghistories.models import SellingHistory


class SellingHistoryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'selling_history_update.html'
    form_class = SellingHistoryForm
    model = SellingHistory
    permission_required = 'sellinghistories.can_change_sellinghistory'

    def form_valid(self, form):
        sellinghistory = form.save(commit=False)
        sellinghistory_entry = self.get_object()
        product = sellinghistory_entry.product
        product.qty += sellinghistory_entry.qty
        product.save()
        sellinghistory.save()
        sellinghistory_entry_last = self.get_object()
        product_last = sellinghistory_entry_last.product
        product_last.qty -= sellinghistory_entry_last.qty
        product_last.save()
        return HttpResponseRedirect(reverse('sellinghistory:list_sellinghistory'))
