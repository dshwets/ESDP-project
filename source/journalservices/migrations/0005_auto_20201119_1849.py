# Generated by Django 2.2.13 on 2020-11-19 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalservices', '0004_auto_20201117_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalservice',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviceexecutors.ServiceExecutor', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='journalservice',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelguests.Guest', verbose_name='Гость'),
        ),
        migrations.AlterField(
            model_name='journalservice',
            name='hostel_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelservices.HostelService', verbose_name='Услуга'),
        ),
    ]
