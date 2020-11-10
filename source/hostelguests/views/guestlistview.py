from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from hostelguests.models import Guest


class Guest_list_view(LoginRequiredMixin, ListView):
    template_name = 'guests.html'
    model = Guest
    context_object_name = 'guests'
    paginate_by = 2
    paginate_orphans = 1