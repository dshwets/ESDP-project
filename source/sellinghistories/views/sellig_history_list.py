from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from sellinghistories.models import SellingHistory


class SellingHistoryListView(PermissionRequiredMixin, ListView):
    template_name = 'sellig_history_list.html'
    queryset = SellingHistory.objects.order_by('-created_at')
    context_object_name = 'sel_his'
    permission_required = 'sellinghistories.can_view_sellinghistory'
    paginate_by = 30
    paginate_orphans = 4