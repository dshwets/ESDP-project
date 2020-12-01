import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText
from documents.models import  Document
from serviceexecutors.factories import ServiceExecutorFactory
from accounts.factories import UserFactory

class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    title = FuzzyText(length=50)
    user = SubFactory(UserFactory)
    file =  factory.django.FileField(filename='the_file.doc')
    service_executor = SubFactory(ServiceExecutorFactory)

