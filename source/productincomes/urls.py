from django.urls import path

from productincomes.views.product_incom_list import ProductIncomesListView

app_name = 'product_incom'

urlpatterns = [
    path('product_incom/', ProductIncomesListView.as_view(), name='list_product_incom'),
]