from django import forms
from django.utils.translation import gettext_lazy as _

from hostelguests.models import Guest

from main.settings import DATE_INPUT_FORMATS

class GuestForm(forms.ModelForm):
    birth_date = forms.DateField(
        input_formats=DATE_INPUT_FORMATS,
        label=_('Дата рождения')
    )
    expiry_passport_date = forms.DateField(
        input_formats=DATE_INPUT_FORMATS,
        required=False,
        label=_('Дата окончания срока действия')
    )


    class Meta:
        model = Guest
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'birth_date',
            'birth_country',
            'passport_id',
            'expiry_passport_date',
            'document_maker',
        ]
