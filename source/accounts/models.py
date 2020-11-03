from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel


class User(AbstractUser, AbstractDatetimeModel):
    position = models.CharField(max_length=255, verbose_name=_('Должность'))

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

