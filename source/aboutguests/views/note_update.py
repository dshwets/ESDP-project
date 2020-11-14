from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from aboutguests.forms import NoteForm
from aboutguests.models import Note


class NoteUpdateView(PermissionRequiredMixin, UpdateView):
    model = Note
    template_name = 'update_note.html'
    form_class = NoteForm
    permission_required = 'aboutguests.can_change_note'

    def get_success_url(self):
        return reverse('hostelguests:detail_view', kwargs={'pk': self.object.guest.pk})