from django.urls import path

from hostelguests.views.guestlistview import Guest_list_view

app_name = 'hostelguests'

urlpatterns = [
    path('', Guest_list_view.as_view(), name='guest_list'),
]