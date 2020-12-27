from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


STATUS_PAYMENT = [
    ('cash', 'Наличный'),
    ('non-cash', 'Безналичный')
]


class ServiceExecutor(AbstractDatetimeModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Имя'),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_('Фамилия'),
    )
    middle_name = models.CharField(
        max_length=255,
        verbose_name=_('Отчество'),
        blank=True,
        default='',
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name=_('Номер телефона'),
    )
    payment = models.CharField(
        max_length=20,
        choices=STATUS_PAYMENT,
        default='cash',
        verbose_name='Тип оплаты'
    )
    hostel_service = models.ForeignKey(
        'hostelservices.HostelService',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='service_executors',
        verbose_name=_('Услуга'),
    )

    class Meta:
        verbose_name = _('Исполнитель')
        verbose_name_plural = _('Исполнители')

        permissions = [
            ('can_add_serviceexecutor', _('Может добавлять исполнителя')),
            ('can_change_serviceexecutor', _('Может изменять исполнителя')),
            ('can_delete_serviceexecutor', _('Может удалять исполнителя')),
            ('can_view_serviceexecutor', _('Может просматривать исполнителя')),
        ]


auditlog.register(ServiceExecutor)
