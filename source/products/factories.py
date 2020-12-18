import factory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyDecimal

from products.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = FuzzyText(length=50)
    qty = FuzzyInteger(0, 100)
    barcode = FuzzyInteger(0, 9999)
    selling_price = FuzzyDecimal(0, 400)
    purchase_price = FuzzyDecimal(0, 400)
