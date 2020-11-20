import factory
from factory import SubFactory
from factory.fuzzy import FuzzyText

from welcomeguests.models import WelcomeGuest

from hostelguests.factories import GuestFactory


class WelcomeGuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WelcomeGuest

    description = FuzzyText(length=50)
    guest = SubFactory(GuestFactory)