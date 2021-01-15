from django import forms
from django.utils.translation import gettext_lazy as _

from products.models import Product
from sellinghistories.carthelper import Cart
from sellinghistories.models import SellingHistory


class AddProductToCartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AddProductToCartForm, self).__init__(*args, **kwargs)

    barcode = forms.IntegerField(label=_('Штрихкод'))
    qty = forms.IntegerField(label=_('Количество'), initial=1)

    class Meta:
        model = SellingHistory
        fields = ['barcode', 'qty']

    def clean_barcode(self):
        barcode = self.cleaned_data.get('barcode')

        existing = Product.objects.filter(
            barcode=barcode
        ).exists()

        if not existing:
            raise forms.ValidationError(_("Данный товар в базе не найден"))

        return barcode

    def save(self, commit=False):
        new_cart_entry = {
            'product_pk': Product.objects.get(barcode=self.cleaned_data['barcode']).pk,
            'qty': self.cleaned_data['qty']
        }
        cart = Cart(self.user.pk)
        cart.add_product(new_cart_entry)

    class SellingHistoryForm(forms.ModelForm):
        class Meta:
            model = SellingHistory
            fields = ['qty', 'selling_price']
