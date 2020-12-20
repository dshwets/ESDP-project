from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import redis
import json

from products.models import Product
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
        red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        cart_entry = {
            'product_pk': Product.objects.get(barcode=self.cleaned_data['barcode']).pk,
            'qty': self.cleaned_data['qty']}
        red.lpush(f'сart:{self.user.pk}', json.dumps(cart_entry))
