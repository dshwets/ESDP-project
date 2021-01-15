from django.core.mail import send_mail


def send_happybirthday_email(name: str, email: list):
    send_mail(
        'Поздравление с Днем Рождения от комманды AppleHostel',
        f'Уважаемый(ая) {name}, от лица всего коллектива отлея AppleHostel, хотели бы поздравить вас с Днем Рождения!\
        Хотели бы пожелать Вам в этот прекрасный день достижения всех ваших целей, успеха в делах и много много \
        денег ;)\n\n \
        С уважением, комманда AppleHostel!',
        'applehostel2020@gmail.com',
        [email]
    )
