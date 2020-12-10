import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText

from hostelguests.factories import GuestFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from journalservices.models import JournalService
from serviceexecutors.factories import ServiceExecutorFactory


class UnwelcomeGuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JournalService

    guest = SubFactory(GuestFactory)
    hostel_service = SubFactory(HostelServiceFactory)
    service_executor = SubFactory(ServiceExecutorFactory)
    purchase_price = SubFactory(PurchasePriceFactory)
    selling_price = SubFactory(SellingPriceFactory)