from auditlog.registry import auditlog
from django.db import models
from django.utils.datetime_safe import datetime

from common.models import AbstractCreatedByModel
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class GuestBirthdayManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(birth_date__day=datetime.now().day, birth_date__month=datetime.now().month)


class Guest(AbstractCreatedByModel):
    first_name = models.CharField(
        max_length=255,
        verbose_name=_('Имя'),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_('Фамилия'),
    )
    middle_name = models.CharField(
        max_length=255,
        default="",
        blank=True,
        verbose_name=_('Отчество'),
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to='guest_photos',
        verbose_name=_('Фото'),
    )
    birth_date = models.DateField(
        verbose_name=_("Дата рождения"),
    )
    birth_country = CountryField(
        blank_label=_('Страна рождения'),
    )
    passport_id = models.CharField(
        max_length=255,
        verbose_name=_('Номер паспорта'),
    )
    expiry_passport_date = models.DateField(
        verbose_name=_('Дата окончания срока действия'),
        null=True,
        blank=True,
    )
    document_maker = models.CharField(
        max_length=255,
        verbose_name=_('Орган выдавший документ'),
        default="",
        blank=True,
    )
    phone = PhoneNumberField(
        blank=True,
        default="",
        verbose_name=_('Контактный номер телефона'),
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_('Email'),
    )

    objects = models.Manager()
    birthdays_guest = GuestBirthdayManager()

    class Meta:
        verbose_name = _('Гость')
        verbose_name_plural = _('Гости')

        permissions = [
            ('can_add_guest', _('Может добавлять гостя')),
            ('can_change_guest', _('Может изменять гостя')),
            ('can_delete_guest', _('Может удалять гостя')),
            ('can_view_guest', _('Может просматривать гостя')),
        ]


auditlog.register(Guest)
