import factory
from serviceexecutors.models import ServiceExecutor
from hostelservices.factories import HostelServiceFactory


class ServiceExecutorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceExecutor

    name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    middle_name = factory.Faker('first_name')
    hostel_service = factory.SubFactory(HostelServiceFactory)
