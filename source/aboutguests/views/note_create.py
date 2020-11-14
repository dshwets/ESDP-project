from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from aboutguests.forms import NoteForm
from aboutguests.models import Note
from hostelguests.models import Guest


class NoteCreateView(PermissionRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'create_note.html'
    permission_required = 'aboutguests.can_add_note'

    def form_valid(self, form):
        guest = get_object_or_404(Guest, pk=self.kwargs.get('guest_pk'))
        note = form.save(commit=False)
        note.guest = guest
        note.save()
        return redirect(
            'hostelguests:detail_view',
            pk=guest.pk
        )