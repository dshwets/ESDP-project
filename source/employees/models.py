from django.db import models
from auditlog.registry import auditlog
from django.utils.translation import gettext_lazy as _
from common.models import AbstractCreatedByModel
from phonenumber_field.modelfields import PhoneNumberField


class Employee(AbstractCreatedByModel):
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
    passport_id = models.CharField(
        max_length=255,
        verbose_name=_('Номер паспорта'),
    )
    phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона'),
    )
    relative_phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона родственника'),
    )
    labor_contract = models.FileField(
        null=True,
        blank=True,
        upload_to='labor_contracts',
        verbose_name=_('Трудовой договор'),
    )
    passport = models.ImageField(
        null=True,
        blank=True,
        upload_to='passport_photos',
        verbose_name=_('Копия паспорта'),
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to='employee_photos',
        verbose_name=_('Фото сотрудника'),
    )
    achievement = models.TextField(
        max_length=255,
        verbose_name=_('Достижения'),
        default="",
        blank=True,
    )
    deposit_amount = models.IntegerField(
        verbose_name=_('Сумма депозита'),
        default="",
        blank=True,
    )
    medical_record = models.BooleanField(
        default=True,
    )
    address = models.TextField(
        default='',
        verbose_name=_('Адрес'),
    )
    note = models.TextField(
        default='',
        verbose_name=_('Примечание'),
    )

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')

        permissions = [
            ('can_add_employee', _('Может добавлять сотрудника')),
            ('can_change_employee', _('Может изменять сотрудника')),
            ('can_delete_employee', _('Может удалять сотрудника')),
            ('can_view_employee', _('Может просматривать сотрудника')),
        ]

auditlog.register(Employee)