from auditlog.registry import auditlog
from django.db import models
from common.models import AbstractCreatedByModel
from django.utils.translation import gettext_lazy as _


class Product(AbstractCreatedByModel):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Название продукта'),
    )
    qty = models.IntegerField(
        default=0,
        verbose_name=_('Количество'),
    )
    barcode = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Штрих код'),
    )
    selling_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Цена продажи')
    )
    purchase_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Цена закупки')
    )
    deleted = models.BooleanField(
        default=False,
        verbose_name=_('Удален')
    )

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

        permissions = [
            ('can_add_product', _('Может добавлять продукт')),
            ('can_change_product', _('Может изменять продукт')),
            ('can_delete_product', _('Может удалять продукт')),
            ('can_view_product', _('Может просматривать продукт')),
        ]


auditlog.register(Product)
