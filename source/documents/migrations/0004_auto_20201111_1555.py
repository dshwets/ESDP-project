# Generated by Django 2.2.13 on 2020-11-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20201111_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='docs', verbose_name='Файл'),
        ),
    ]
