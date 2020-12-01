from django.urls import path

from documents.views.document_update import DocumentUpdateView

app_name = 'documents'

urlpatterns = [
    path('documents/<int:pk>/update/', DocumentUpdateView.as_view(), name='document_update'),
]
