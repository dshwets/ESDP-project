from auditlog.registry import auditlog
from django.db import models
from common.models import AbstractCreatedByModel
from django.utils.translation import gettext_lazy as _


class WelcomeGuest(AbstractCreatedByModel):
    guest = models.OneToOneField(
        'hostelguests.Guest',
        on_delete=models.CASCADE,
        verbose_name=_('Гость'),
    )
    description = models.TextField(
        max_length=2000,
        verbose_name=_('Описание'),
        blank=True,
    )

    class Meta:
        verbose_name = _('Желанный гость')
        verbose_name_plural = _('Желанные гости')

        permissions = [
            ('can_add_welcomeguest', _('Может добавлять желанного гостя')),
            ('can_change_welcomeguest', _('Может изменять желанного гостя')),
            ('can_delete_welcomeguest', _('Может удалять желанного гостя')),
            ('can_view_welcomeguest', _('Может просматривать желанного гостя')),
        ]

    def __str__(self):
        return "{}. {}".format(self.guest.first_name, self.guest.last_name)

auditlog.register(WelcomeGuest)
