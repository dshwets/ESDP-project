from auditlog.registry import auditlog
from django.db import models
from common.models import AbstractDatetimeModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Document(AbstractDatetimeModel):
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Название'),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
    )
    file = models.FileField(
        upload_to='docs',
        verbose_name=_('Файл'),
    )

    class Meta:
        verbose_name = _('Документ')
        verbose_name_plural = _('Документы')

        permissions = [
            ('can_add_document', _('Может добавлять документ')),
            ('can_change_document', _('Может изменять документ')),
            ('can_delete_document', _('Может удалять документ')),
            ('can_view_document', _('Может просматривать документ')),
        ]


auditlog.register(Document)