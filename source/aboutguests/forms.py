from django import forms

from aboutguests.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['description',]
