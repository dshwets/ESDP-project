from django.urls import reverse
from django.views.generic import CreateView

from products.models import Product
from sellinghistories.forms import SellinghistoryForm
from sellinghistories.models import SellingHistory


class AddProductToCartView(CreateView):
    template_name = 'sellinghistory_create.html'
    form_class = SellinghistoryForm
    model = SellingHistory
    permission_required = 'sellinghistory.can_add_sellinghistory'

    def get_form_kwargs(self):
        kwargs = super(AddProductToCartView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def get_success_url(self):
        return reverse('sellinghisoty:add_product_in_cart')
