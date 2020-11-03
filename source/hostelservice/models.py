from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


class HostelService(AbstractDatetimeModel):
    name = models.CharField(max_length=500, verbose_name=_('Наименование услуги'))
    price = models.DecimalField(verbose_name=_('Цена'))

    class Meta:
        abstract = True