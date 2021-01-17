from django.core.mail import send_mail
from django.utils.datetime_safe import datetime

from hostelguests.models import Guest


def send_happybirthday_email(name: str, emails: list):
    send_mail(
        'Поздравление с Днем Рождения от комманды AppleHostel',
        f'Уважаемый(ая) {name}, от лица всего коллектива отеля AppleHostel, хотели бы поздравить вас с Днем Рождения!\
        Хотели бы пожелать Вам в этот прекрасный день достижения всех ваших целей, успеха в делах и много много \
        денег ;)\n\n \
С уважением, комманда AppleHostel!',
        'applehostel2020@gmail.com',
        emails
    )


def get_birthday_people():
    now = datetime.now()
    birthdays_people = Guest.objects.filter(birth_date__day=now.day, birth_date__month=now.month)
    return birthdays_people
