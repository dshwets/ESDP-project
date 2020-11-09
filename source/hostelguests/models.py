from django.db import models
from common.models import AbstractDatetimeModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Guest(AbstractDatetimeModel):
    first_name = models.CharField(max_length=255,verbose_name=_('Имя'))
    last_name = models.CharField(max_length=255, verbose_name=_('Фамилия'))
    middle_name = models.CharField(max_length=255,default="", verbose_name=_('Отчество'))
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                   null=True, verbose_name=_('Кем создано'))
    photo = models.ImageField(null=True, blank=True, upload_to='guest_photos', verbose_name=_('Фото'))
    birth_date = models.DateField(verbose_name=_("Дата рождения"))
    birth_country = models.CharField(max_length=255, verbose_name=_('Страна рождения'))
    passport_id = models.CharField(max_length=255, verbose_name=_('Номер паспорта'))
    expiry_passport_date = models.DateField(verbose_name=_('Дата окончания срока действия'), null=True)
    document_maker = models.CharField(max_length=255, verbose_name=_('Орган выдавший документ'), default="")

    class Meta:
        verbose_name = _('Гость')
        verbose_name_plural = _('Гости')