from django.shortcuts import get_object_or_404

from hostelguests.models import Guest
from journalservices.models import JournalService
from django import forms


class JournalServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        guest_id = kwargs.pop('guest_id')
        self.guest = get_object_or_404(Guest, pk=guest_id)
        super(JournalServiceForm, self).__init__(*args, **kwargs)

    guest = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = JournalService
        fields = ['guest',
                  'hostel_service',
                  'service_executor',
                  'purchase_price',
                  'selling_price', ]

    def clean_guest(self):
        guest = self.guest
        return guest
