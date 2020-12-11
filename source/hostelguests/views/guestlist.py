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
    ordering = '-id'
    paginate_by = 10
    paginate_orphans = 4
    allow_empty = True

    def get_queryset(self):
        queryset = super().get_queryset()
        request_path = str(self.request).split('?')
        try:
            if 'ordering' in request_path[1]:
                queryset = queryset.order_by('last_name', 'first_name')
            return queryset
        except IndexError:
            return queryset

