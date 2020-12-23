from django.urls import path

from sellinghistories.views.sellinghistory_create import AddProductToCartView, CreateSellingHistory
from sellinghistories.views.sellinghistory_delete import DeletePRoductFromCart

app_name = 'sellinghisoty'

urlpatterns = [
    path('sellinghistory/add/', AddProductToCartView.as_view(), name='add_product_in_cart'),
    path('sellinghistory/create/', CreateSellingHistory.as_view(), name='create_sellinghistory'),
    path('sellinghistory/<int:pk>/remove_from_cart', DeletePRoductFromCart.as_view(), name='remove_product_from_cart')
]
