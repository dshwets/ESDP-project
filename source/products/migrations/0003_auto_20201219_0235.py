# Generated by Django 2.2.13 on 2020-12-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201218_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='Штрих код'),
        ),
    ]