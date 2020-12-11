from django.urls import path

from journalservices.views.journalservice_list import JournalServicesListView

app_name = 'journalservices'

urlpatterns = [
    path('journal/', JournalServicesListView.as_view(), name='journal_list'),
]