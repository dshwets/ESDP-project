from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from unwelcomeguests.models import UnwelcomeGuest


class UnwelcomeGuestListView(LoginRequiredMixin, ListView):
    template_name = 'unwelcomeguest_list.html'
    queryset = UnwelcomeGuest.objects.all()
    context_object_name = 'unwelcome_guests'
    paginate_by = 10
    paginate_orphans = 4

