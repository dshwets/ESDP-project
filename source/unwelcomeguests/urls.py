from django.urls import path

from unwelcomeguests.views.unwelcomeguest_delete import UnwelcomeGuestDeleteView
from unwelcomeguests.views.unwelcomeguest_list import UnwelcomeGuestListView

app_name = 'unwelcomeguests'

urlpatterns = [
    path('unwelcomeguests/<int:pk>/delete/', UnwelcomeGuestDeleteView.as_view(), name='unwelcomeguest_delete'),
    path('unwelcomeguests/', UnwelcomeGuestListView.as_view(), name='unwelcome_guest_list'),
]