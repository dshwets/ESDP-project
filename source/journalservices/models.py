from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel



class JournalService(AbstractDatetimeModel):
    guest = models.ManyToManyField(
        'hostelguests.Guest',
        verbose_name=_('Гость'),
    )
    hostel_service=models.ManyToManyField(
        'hostelservices.HostelService',
        verbose_name=_('Услуга'),
    )
    executor=models.ManyToManyField(
        'serviceexecutors.ServiceExecutor',
        verbose_name=_('Исполнитель'),
    )

    class Meta:
        verbose_name = _('Журнал услуг')
        verbose_name_plural = _('Журналы услуг')

