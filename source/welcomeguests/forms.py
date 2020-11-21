from django import forms
from welcomeguests.models import WelcomeGuest


class WelcomeGuestForm(forms.ModelForm):

    class Meta:
        model = WelcomeGuest
        fields = [
            'description'
        ]
