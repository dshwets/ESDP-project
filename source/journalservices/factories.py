import factory
from factory import SubFactory

from hostelguests.factories import GuestFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from journalservices.models import JournalService
from serviceexecutors.factories import ServiceExecutorFactory


class JournalServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JournalService

    guest = SubFactory(GuestFactory)
    hostel_service = SubFactory(HostelServiceFactory)
    service_executor = SubFactory(ServiceExecutorFactory)
    purchase_price = SubFactory(PurchasePriceFactory)
    selling_price = SubFactory(SellingPriceFactory)