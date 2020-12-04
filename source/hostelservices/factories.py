import factory
from factory.fuzzy import FuzzyText

from hostelservices.models import HostelService


class HostelServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HostelService

    service_name = FuzzyText(length=50)