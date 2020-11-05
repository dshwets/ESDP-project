from django.db import models
from common.models import AbstractDatetimeModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class UnwelcomeGuest(AbstractDatetimeModel):
    guest = models.ForeignKey(
        'hostelguests.Guest',
        on_delete=models.CASCADE,
        verbose_name=_('Гость'),
    )
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Кем создано'),
    )
    description = models.TextField(
        max_length=2000,
        verbose_name=_('Описание'),
        blank=True,
    )

    class Meta:
        verbose_name = _('Нежеланный гость')
        verbose_name_plural = _('Нежеланные гости')

