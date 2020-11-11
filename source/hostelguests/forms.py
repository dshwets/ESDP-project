from django import forms
from hostelguests.models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name',
                  'last_name',
                  'middle_name',
                  'created_by',
                  'photo',
                  'birth_date',
                  'birth_country',
                  'passport_id',
                  'expiry_passport_date',
                  'document_maker']
