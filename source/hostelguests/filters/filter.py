import django_filters
from django.db.models import Q
from django import forms

from hostelguests.models import Guest


class GuestFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='my_filter', label='', widget=forms.TextInput(attrs={'class': "form-control mr-sm-2"}))

    class Meta:
        model = Guest
        fields = ['search']

    def my_filter(self, queryset, name, value):
        print(value)
        return Guest.objects.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value) |
            Q(middle_name__icontains=value)
        )
