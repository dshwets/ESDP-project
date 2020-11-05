# Generated by Django 2.2.13 on 2020-11-05 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostelguests', '0002_auto_20201105_0920'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelguests.Guest', verbose_name='Гость')),
            ],
            options={
                'verbose_name': 'Желанный гость',
                'verbose_name_plural': 'Желанные гости',
            },
        ),
    ]
