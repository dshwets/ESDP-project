import factory
from factory.fuzzy import FuzzyText
from employees.models import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    created_by = None
    passport_id = '123456789'
    phone_number = '+996500500500'
    relative_phone_number = '+996500500501'
    labor_contract = factory.django.FileField(filename='the_file.doc')
    passport = factory.django.FileField(filename='the_file.doc')
    achievement = FuzzyText(length=25)
    deposit_amount = '500'
    medical_record = False
    address = '150 Ahunbaeva street, 79'
    note = FuzzyText(length=50)