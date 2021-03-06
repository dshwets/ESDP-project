import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText

from aboutguests.models import Note

from hostelguests.factories import GuestFactory


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    description = FuzzyText(length=50)
    guest = SubFactory(GuestFactory)
