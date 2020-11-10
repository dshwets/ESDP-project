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

        permissions = [
            ('can_add_journalservice', _('Может добавлять журнал услуг')),
            ('can_change_journalservice', _('Может изменять журнал услуг')),
            ('can_delete_journalservice', _('Может удалять журнал услуг')),
            ('can_view_journalservice', _('Может просматривать журнал услуг')),
        ]
