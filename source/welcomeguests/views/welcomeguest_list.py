from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from welcomeguests.models import WelcomeGuest


class WelcomeGuestListView(LoginRequiredMixin, ListView):
    template_name = '#'
    model = WelcomeGuest
    context_object_name = 'welcome_guests'
    paginate_by = 10
    paginate_orphans = 4