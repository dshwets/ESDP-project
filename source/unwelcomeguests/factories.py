import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText

from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from unwelcomeguests.models import UnwelcomeGuest


class UnwelcomeGuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UnwelcomeGuest

    guest = SubFactory(GuestFactory)
    created_by =SubFactory(UserFactory)
    description = FuzzyText(length=50)
