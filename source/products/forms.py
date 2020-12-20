from django import forms

from accounts.models import User
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['deleted', 'created_by']

    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('created_by', None)
        created_by = User.objects.all().filter(pk=user_pk).first()
        self.created_by = created_by
        super(ProductForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        object = super(ProductForm, self).save(commit=False)
        object.created_by = self.created_by
        if commit:
            object.save()
        return object