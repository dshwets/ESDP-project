from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractDatetimeModel, AbstractCreatedByModel


class HostelService(AbstractDatetimeModel):
    service_name = models.CharField(max_length=255, verbose_name=_('Наименование услуги'))

    class Meta:
        verbose_name = _('Услуга отеля')
        verbose_name_plural = _('Услуги отеля')

        permissions = [
            ('can_add_hostelservice', _('Может добавлять услугу отеля')),
            ('can_change_hostelservice', _('Может изменять услугу отеля')),
            ('can_delete_hostelservice', _('Может удалять услугу отеля')),
            ('can_view_hostelservice', _('Может просматривать услугу отеля')),
        ]

    def __str__(self):
        return f'{self.service_name}'


class SellingPrice(AbstractCreatedByModel):
    selling_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name=_('Цена продажи')
    )
    hostel_service = models.ForeignKey(
        'hostelservices.HostelService',
        null=True,
        on_delete=models.CASCADE,
        related_name='selling_price',
        verbose_name=_('Услуга отеля'),
    )

    class Meta:
        verbose_name = _('Цена продажи')
        verbose_name_plural = _('Цены продажи')

        permissions = [
            ('can_add_selling_price', _('Может добавлять цену продажи')),
            ('can_change_selling_price', _('Может изменять цену продажи')),
            ('can_delete_selling_price', _('Может удалять цену продажи')),
            ('can_view_selling_price', _('Может просматривать цену продажи')),
        ]


class PurchasePrice(AbstractCreatedByModel):
    purchase_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Цена покупки')
    )
    hostel_service = models.ForeignKey(
        'hostelservices.HostelService',
        null=True,
        on_delete=models.CASCADE,
        related_name='purchase_price',
        verbose_name=_('Услуга отеля'),
    )
    class Meta:
        verbose_name = _('Цена покупки')
        verbose_name_plural = _('Цены покупки')

        permissions = [
            ('can_add_purchase_price', _('Может добавлять цену покупки')),
            ('can_change_purchase_price', _('Может изменять цену покупки')),
            ('can_delete_purchase_price', _('Может удалять цену покупки')),
            ('can_view_purchase_price', _('Может просматривать цену покупки')),
        ]


auditlog.register(HostelService)
