# Generated by Django 2.2.13 on 2020-12-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Штрих код'),
        ),
    ]