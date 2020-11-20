from django import forms
from unwelcomeguests.models import UnwelcomeGuest


class UnWelcomeGuestForm(forms.ModelForm):

    class Meta:
        model = UnwelcomeGuest
        fields = [
            'description'
        ]