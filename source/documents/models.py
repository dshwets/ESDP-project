from django.db import models
from common.models import AbstractDatetimeModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Document(AbstractDatetimeModel):
    title = models.CharField(max_length=255, blank=True, verbose_name=_('Название'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    pic = models.FileField(upload_to='docs', verbose_name=_('Документ'))

    class Meta:
        verbose_name = _('Документ')
        verbose_name_plural = _('Документы')