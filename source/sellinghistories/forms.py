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
        updated = False
        red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        new_cart_entry = {
            'product_pk': Product.objects.get(barcode=self.cleaned_data['barcode']).pk,
            'qty': self.cleaned_data['qty']
        }
        redis_list = red.lrange(f'cart:{self.user.pk}', 0, -1)
        for redis_list_entry in redis_list:
            redis_list_entry_as_dict = json.loads(redis_list_entry)
            if redis_list_entry_as_dict["product_pk"] == new_cart_entry["product_pk"]:
                redis_list_entry_as_dict['qty'] += new_cart_entry['qty']
                index = redis_list.index(redis_list_entry)
                redis_list_entry = json.dumps(redis_list_entry_as_dict)
                red.lset(f'cart:{self.user.pk}', index, redis_list_entry)
                red.expire(f'cart:{self.user.pk}', 3600)
                updated = True
        if not updated:
            red.lpush(f'cart:{self.user.pk}', json.dumps(new_cart_entry), )
            red.expire(f'cart:{self.user.pk}', 3600)
