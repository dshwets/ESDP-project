# Generated by Django 2.2.13 on 2020-11-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcomeguests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcomeguest',
            name='description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Описание'),
        ),
    ]
