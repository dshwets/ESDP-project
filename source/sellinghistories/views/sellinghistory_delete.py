from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView

from sellinghistories.models import SellingHistory


class SellingHistoryDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'sellinghistory_delete.html'
    model = SellingHistory
    permission_required = 'sellinghistories.can_delete_sellinghistory'

    def get_success_url(self):
        return reverse('sellinghistory:list_sellinghistory')

    def delete(self, request, *args, **kwargs):
        sellinghistory_entry = self.get_object()
        product = sellinghistory_entry.product
        product.qty += sellinghistory_entry.qty
        product.save()
        return super(SellingHistoryDeleteView, self).delete(request, *args, **kwargs)
