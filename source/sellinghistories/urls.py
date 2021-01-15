from django.urls import path

from sellinghistories.views.sellig_history_list import SellingHistoryListView
from sellinghistories.views.selling_history_update import SellingHistoryUpdateView
from sellinghistories.views.sellinghistory_create import AddProductToCartView, CreateSellingHistory
from sellinghistories.views.delete_product_from_cart import DeleteProductFromCart
from sellinghistories.views.sellinghistory_delete import SellingHistoryDeleteView

app_name = 'sellinghistory'

urlpatterns = [
    path('sellinghistory/add/', AddProductToCartView.as_view(), name='add_product_in_cart'),
    path('sellinghistory/create/', CreateSellingHistory.as_view(), name='create_sellinghistory'),
    path('sellinghistory/', SellingHistoryListView.as_view(), name='list_sellinghistory'),
    path('sellinghistory/<int:pk>/remove_from_cart', DeleteProductFromCart.as_view(), name='remove_product_from_cart'),
    path('sellinghistory/<int:pk>/delete/', SellingHistoryDeleteView.as_view(), name='sellinghistory_delete'),
    path('sellinghistory/<int:pk>/update/', SellingHistoryUpdateView.as_view(), name='sellinghistory_update'),
]
