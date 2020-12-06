from betterforms.multiform import MultiModelForm
from django.forms import ModelForm, forms
from django.forms.models import inlineformset_factory

from .models import HostelService, SellingPrice, PurchasePrice


class HostelServiceForm(ModelForm):
    class Meta:
        model = HostelService
        fields = ('service_name',)


class SellingPriceForm(ModelForm):
    class Meta:
        model = SellingPrice
        fields = ('selling_price',)


class PurchasePriceForm(ModelForm):
    class Meta:
        model = PurchasePrice
        fields = ('purchase_price',)


class HostelServiceMultiForm(MultiModelForm):
    form_classes = {
        'service_name': HostelServiceForm,
        'selling_price': SellingPriceForm,
        'purchase_price': PurchasePriceForm,
    }
