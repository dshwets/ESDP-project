from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import FilterView

from hostelguests.filters.filter import GuestSearch
from hostelguests.models import Guest


class GuestListView(LoginRequiredMixin, FilterView):
    template_name = 'guests.html'
    model = Guest
    filterset_class = GuestSearch
    context_object_name = 'guests'
    paginate_by = 10
    paginate_orphans = 4
