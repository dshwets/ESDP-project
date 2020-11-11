from django.urls import path

from hostelguests.views.guestlist import GuestListView

app_name = 'hostelguests'

urlpatterns = [
    path('', GuestListView.as_view(), name='guest_list'),
]