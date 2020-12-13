from journalservices.models import JournalService
from django import forms

class JournalServiceForm(forms.ModelForm):
    class Meta:
        model = JournalService
        exclude = ['guest']