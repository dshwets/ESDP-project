from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


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
        default='',
    )
    document = models.ForeignKey(
        'documents.Document',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Документ'),
    )

    class Meta:
        verbose_name = _('Исполнитель')
        verbose_name_plural = _('Исполнители')





