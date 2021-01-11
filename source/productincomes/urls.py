from django.urls import path

from productincomes.views.product_incom_create import IndexView
from productincomes.views.product_incom_list import ProductIncomesListView
from productincomes.views.product_income_detail import ProductIncomesDetailView

app_name = 'product_incom'

urlpatterns = [
    path('product_incom/', ProductIncomesListView.as_view(), name='list_product_incom'),
    path('product_incom/create/', IndexView.as_view(), name='product_incom_create'),
    path('product_incom/<int:pk>/', ProductIncomesDetailView.as_view(), name='product_incom_detail'),
]