from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from sellinghistories.forms import SellingHistoryForm
from sellinghistories.models import SellingHistory


class SellingHistoryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'selling_history_update.html'
    form_class = SellingHistoryForm
    model = SellingHistory
    permission_required = 'serviceexecutors.can_change_sellinghistory'

    def get_success_url(self):
        return reverse('', kwargs={'pk': self.object.pk})