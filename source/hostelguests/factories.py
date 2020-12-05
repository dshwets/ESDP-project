import factory
from hostelguests.models import Guest
from django.utils import timezone


class GuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Guest

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    created_by = None
    birth_date = timezone.localdate()
    birth_country = 'KG'
    passport_id = '123456789'
    expiry_passport_date = None