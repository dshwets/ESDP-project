import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText, FuzzyDecimal
from hostelservices.models import HostelService, PurchasePrice, SellingPrice


class HostelServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HostelService

    service_name = FuzzyText(length=50)


class SellingPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SellingPrice

    selling_price = FuzzyDecimal(0, 500)
    hostel_service = SubFactory(HostelServiceFactory)


class PurchasePriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PurchasePrice

    purchase_price = FuzzyDecimal(0, 400)
    hostel_service = SubFactory(HostelServiceFactory)


def correct_service_factory():
    hostel_service = HostelServiceFactory()
    SellingPriceFactory(hostel_service=hostel_service)
    PurchasePriceFactory(hostel_service=hostel_service)