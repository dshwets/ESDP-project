from django.db import models
from django.utils.translation import gettext_lazy as _
from auditlog.registry import auditlog
from common.models import AbstractCreatedByModel
from django.core.validators import MinValueValidator


class SellingHistory(AbstractCreatedByModel):
    qty = models.IntegerField(
        default=0,
        verbose_name=_('Количество'),
        validators=[MinValueValidator(0)],
    )
    guest = models.ForeignKey(
        'hostelguests.Guest',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Гость'),
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        verbose_name=_('Продукт'),
    )
    purchase_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_('Цена закупки'),
    )
    selling_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_('Цена продажи'),
    )

    class Meta:
        verbose_name = _('Запись продажи')
        verbose_name_plural = _('Записи продаж')

        permissions = [
            ('can_add_sellinghistory', _('Может добавлять запись продажи')),
            ('can_change_sellinghistory', _('Может изменять запись продажи')),
            ('can_delete_sellinghistory', _('Может удалять запись продажи')),
            ('can_view_sellinghistory', _('Может просматривать запись продажи')),
        ]

auditlog.register(SellingHistory)
