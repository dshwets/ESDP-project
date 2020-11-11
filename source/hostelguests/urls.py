from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from hostelguests.views.guest_create_view import GuestCreateView

app_name = 'hostelguests'

urlpatterns = [
    path('guest/add/', GuestCreateView.as_view(), name='guest_create'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)