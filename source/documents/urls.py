from django.urls import path

from documents.views.document_add import DocumentExecutorCreateView
from documents.views.document_delete import DocumentDeleteView
from documents.views.document_update import DocumentUpdateView

app_name = 'documents'

urlpatterns = [
    path('documents/<int:pk>/update/', DocumentUpdateView.as_view(), name='document_update'),
    path('documents/<int:pk>/delete', DocumentDeleteView.as_view(), name='document_delete'),
    path('serviceexecutors/<int:pk>/documents_add', DocumentExecutorCreateView.as_view(), name='doc_add')
]
