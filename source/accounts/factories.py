import factory
from factory import PostGenerationMethodCall, Sequence

from accounts.models import User
from django.utils import timezone


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: f'Username{n}')
    password = PostGenerationMethodCall('set_password', 'pass')
