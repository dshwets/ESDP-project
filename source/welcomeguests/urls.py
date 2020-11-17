from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from welcomeguests.views.welcomeguest_list import WelcomeGuestListView

app_name = 'welcomeguests'

urlpatterns = [
    path('welcomeguest/', WelcomeGuestListView.as_view(), name='welcome_guest_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)