from auditlog.registry import auditlog
from django.db import models
from common.models import AbstractCreatedByModel
from django.utils.translation import gettext_lazy as _


class Incomes(AbstractCreatedByModel):
    services_executor = models.ForeignKey(
        'serviceexecutors.ServiceExecutor',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Поставщик'),
    )

    class Meta:
        verbose_name = _('Приход')
        verbose_name_plural = _('Приходы')

        permissions = [
            ('can_add_incomes', _('Может создавать приход')),
            ('can_change_incomes', _('Может изменять приход')),
            ('can_delete_incomes', _('Может удалять приход')),
            ('can_view_incomes', _('Может просматривать приход')),
        ]

    def __str__(self):
        return f'{self.services_executor} {self.created_at}'


class ProductIncomes(models.Model):
    incomes = models.ForeignKey(
        'productincomes.Incomes',
        on_delete=models.CASCADE,
        related_name='product_incomes',
        verbose_name=_('Приход товара'),
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
            ('can_add_product_incomes', _('Может создавать приход товара')),
            ('can_change_product_incomes', _('Может изменять приход товара')),
            ('can_delete_product_incomes', _('Может удалять приход товара')),
            ('can_view_product_incomes', _('Может просматривать приход товара')),
        ]

    def __str__(self):
        return f'{self.incomes.services_executor} {self.product}'
auditlog.register(ProductIncomes)