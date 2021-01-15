from main.celery import app

from common.services.send_email import send_happybirthday_email,get_birthday_people


@app.task
def send_emails():
    birthday_list = get_birthday_people()
    for birthday_body in birthday_list:
        send_happybirthday_email(birthday_body.first_name, [birthday_body.email])
