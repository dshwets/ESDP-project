from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.product_detail_api import ProductDetailView, ProductIncomeView

app_name = 'api'

urlpatterns = [
    path('api/product_barcode/<int:barcode>/', ProductDetailView.as_view(), name='barcode_product'),
    path('api/incoming_product/', ProductIncomeView.as_view(), name='product_incoming_create'),
]