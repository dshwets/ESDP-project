from django.urls import path

from products.views.product_create import ProductCreateView
from products.views.product_list import ProductListView

app_name = 'products'

urlpatterns = [
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
]
