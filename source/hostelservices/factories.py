import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText

from hostelservices.models import HostelService, PurchasePrice, SellingPrice


class HostelServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HostelService

    service_name = FuzzyText(length=50)


class SellingPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SellingPrice

    selling_price = FuzzyText(length=50)
    hostel_service = SubFactory(HostelServiceFactory)

class PurchasePriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PurchasePrice

    purchase_price = FuzzyText(length=50)
    hostel_service = SubFactory(HostelServiceFactory)