from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from hostelguests.views.guest_create_view import GuestCreateView
from django.urls import path

from hostelguests.views.guestlist import GuestListView

app_name = 'hostelguests'

urlpatterns = [
    path('', GuestListView.as_view(), name='guest_list'),
]
    path('guest/add/', GuestCreateView.as_view(), name='guest_create'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)