from django.urls import path

from sellinghistories.views.sellinghistory_create import AddProductToCartView, CreateSellingHistory

app_name = 'sellinghisoty'

urlpatterns = [
    path('sellinghistory/add/', AddProductToCartView.as_view(), name='add_product_in_cart'),
    path('sellinghistory/create/', CreateSellingHistory.as_view(), name='create_sellinghistory'),
]
