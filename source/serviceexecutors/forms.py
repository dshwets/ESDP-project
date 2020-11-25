from django import forms
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorForm(forms.ModelForm):

    class Meta:
        model = ServiceExecutor
        exclude = []
