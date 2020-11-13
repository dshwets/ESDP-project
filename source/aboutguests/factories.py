import factory
from factory.fuzzy import FuzzyText

from aboutguests.models import Note
from django.utils import timezone

from hostelguests.factories import GuestFactory


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    description = FuzzyText(length=50)
    guest = GuestFactory()