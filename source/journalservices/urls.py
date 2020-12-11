from django.urls import path

from journalservices.views.journalservice_list import JournalServicesListView
from journalservices.views.journalservice_detail import JournalServiceDetailView

app_name = 'journalservices'

urlpatterns = [
    path('journal/', JournalServicesListView.as_view(), name='journal_list'),
    path('journal/<int:pk>/', JournalServiceDetailView.as_view(), name='journal_detail'),
]