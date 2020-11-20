from django.urls import path

from unwelcomeguests.views.unwelcomeguest_delete import UnwelcomeGuestDeleteView

app_name = 'unwelcomeguests'

urlpatterns = [
    path('unwelcomeguests/<int:pk>/delete/', UnwelcomeGuestDeleteView.as_view(), name='unwelcomeguest_delete'),

]