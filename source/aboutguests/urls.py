from django.urls import path

from aboutguests.views.note_create import NoteCreateView

app_name = 'aboutguests'

urlpatterns = [
    path('add/', NoteCreateView.as_view(), name='note_create'),
]