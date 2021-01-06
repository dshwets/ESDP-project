from django import forms
from django.utils.translation import gettext_lazy as _

from hostelguests.models import Guest

from django.conf import settings


class GuestForm(forms.ModelForm):
    birth_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        label=_('Дата рождения')
    )
    expiry_passport_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        required=False,
        label=_('Дата окончания срока действия')
    )
    hidden_base64 = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = Guest
        fields = [
            'hidden_base64',
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'phone',
            'email',
            'birth_date',
            'birth_country',
            'passport_id',
            'expiry_passport_date',
            'document_maker',
        ]
        labels = {
            'birth_country': _('Страна рождения'),
        }
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+996000112233'})
        }