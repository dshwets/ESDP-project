import factory
from factory import SubFactory
from factory.fuzzy import FuzzyInteger, FuzzyDecimal

from productincomes.models import Incomes, ProductIncomes
from products.factories import ProductFactory
from serviceexecutors.factories import ServiceExecutorFactory


class IncomesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Incomes

    services_executor = SubFactory(ServiceExecutorFactory)


class ProductIncomesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductIncomes

    incomes = SubFactory(IncomesFactory)
    product = SubFactory(ProductFactory)
    qty = FuzzyInteger(0, 100)
