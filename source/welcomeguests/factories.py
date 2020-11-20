import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText

from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from welcomeguests.models import WelcomeGuest


class WelcomeGuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WelcomeGuest

    guest = SubFactory(GuestFactory)
    created_by =SubFactory(UserFactory)
    description = FuzzyText(length=50)