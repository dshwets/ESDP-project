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
#
# class HostelServiceUpdate(inlineformset_factory(HostelService,SellingPrice,PurchasePrice)):
#     fields = ('service_name', 'selling_price', 'purchase_price')

#
# class HostelServiceUpdate(ModelForm):
#     service_name = models.CharField()
#
#
# class HostelServiceForm(ModelForm):
#     class Meta:
#         model = HostelService
#         fields = ('service_name',)
# #
# #
# SellingPriceFormSet = inlineformset_factory(HostelService, SellingPrice, fields=('selling_price',))
# PurchasePriceFormSet = inlineformset_factory(HostelService, PurchasePrice, fields=('purchase_price',))
