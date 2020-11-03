# Generated by Django 2.2.13 on 2020-11-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostelService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование услуги')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Услуга отеля',
                'verbose_name_plural': 'Услуги отеля',
            },
        ),
    ]
