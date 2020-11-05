from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


class Note(AbstractDatetimeModel):
    note = models.TextField(
        max_length=2000,
        verbose_name=_('Заметки о госте'),)
    guest_id = models.ForeignKey(
        'hostelguests.Guest',
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name=_('Гость'))

    class Meta:
        verbose_name = _('Заметка о госте')
        verbose_name_plural = _('Заметки о госте')
