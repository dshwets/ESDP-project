# Generated by Django 2.2.13 on 2020-12-08 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostelservices', '0004_auto_20201203_2303'),
        ('serviceexecutors', '0003_remove_serviceexecutor_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceexecutor',
            name='hostel_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_executors', to='hostelservices.HostelService', verbose_name='Услуга'),
        ),
    ]
