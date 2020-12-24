import factory
from factory import SubFactory
from factory.fuzzy import FuzzyInteger, FuzzyDecimal

from hostelguests.factories import GuestFactory
from products.factories import ProductFactory
from sellinghistories.models import SellingHistory


class SellingHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SellingHistory

        qty = FuzzyInteger(0, 100)
        guest = SubFactory(GuestFactory)
        product = SubFactory(ProductFactory)
        selling_price = FuzzyDecimal(0, 400)
        purchase_price = FuzzyDecimal(0, 400)