from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


class HostelService(AbstractDatetimeModel):
    name = models.CharField(max_length=255, verbose_name=_('Наименование услуги'))
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=_('Цена'))

    class Meta:
        verbose_name = _('Услуга отеля')
        verbose_name_plural = _('Услуги отеля')

        permissions = [
            ('can_add_hostelservice', _('Может добавлять услугу отеля')),
            ('can_change_hostelservice', _('Может изменять услугу отеля')),
            ('can_delete_hostelservice', _('Может удалять услугу отеля')),
            ('can_view_hostelservice', _('Может просматривать услугу отеля')),
        ]


auditlog.register(HostelService)
