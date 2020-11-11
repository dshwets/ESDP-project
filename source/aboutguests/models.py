from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


class Note(AbstractDatetimeModel):
    description = models.TextField(
        default='',
        verbose_name=_('Описание'),
    )
    guest = models.ForeignKey(
        'hostelguests.Guest',
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name=_('Гость'),
    )

    class Meta:
        verbose_name = _('Заметка о госте')
        verbose_name_plural = _('Заметки о госте')

        permissions = [
            ('can_add_note', _('Может добавлять заметку о госте')),
            ('can_change_note', _('Может изменять заметку о госте')),
            ('can_delete_note', _('Может удалять заметку о госте')),
            ('can_view_note', _('Может просматривать заметку о госте')),
        ]