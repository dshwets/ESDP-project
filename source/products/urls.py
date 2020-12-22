from django.urls import path

from products.views.product_create import ProductCreateView
from products.views.product_delete import ProductDeleteView
from products.views.product_list import ProductListView
from products.views.product_update import ProductUpdateView

app_name = 'products'

urlpatterns = [
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]
