from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from welcomeguests.models import WelcomeGuest


class WelcomeGuestListView(PermissionRequiredMixin, ListView):
    template_name = 'welcomeguest_list.html'
    queryset = WelcomeGuest.objects.all().order_by('created_at')
    permission_required = 'welcome_guests.can_view_welcomeguest'
    context_object_name = 'welcome_guests'
    paginate_by = 10
    paginate_orphans = 4



