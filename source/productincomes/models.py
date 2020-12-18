from auditlog.registry import auditlog
from django.db import models
from common.models import AbstractCreatedByModel
from django.utils.translation import gettext_lazy as _


class ProductIncomes(AbstractCreatedByModel):
    services_executor = models.ForeignKey(
        'serviceexecutors.ServiceExecutor',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Поставщик'),
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        verbose_name=_('Товар'),
    )
    qty = models.IntegerField(
        default=0,
        verbose_name=_('Количество'),
    )

    class Meta:
        verbose_name = _('Приход товара')
        verbose_name_plural = _('Приходы товара')

        permissions = [
            ('can_add_product_incomes', _('Может оприходовать товар')),
            ('can_change_product_incomes', _('Может изменять приход товара')),
            ('can_delete_product_incomes', _('Может удалять приход товара')),
            ('can_view_product_incomes', _('Может просматривать приход товара')),
        ]


auditlog.register(ProductIncomes)