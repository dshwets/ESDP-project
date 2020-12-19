from django.urls import path

from products.views.product_create import ProductCreateView

app_name = 'products'

urlpatterns = [
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
]
