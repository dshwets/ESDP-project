from django.urls import path

from aboutguests.views.note_create import NoteCreateView
from aboutguests.views.note_delete import NoteDeleteView

app_name = 'aboutguests'

urlpatterns = [
    path('guests/<int:guest_pk>/notes/add/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]