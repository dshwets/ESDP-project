# Generated by Django 2.2.13 on 2020-11-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelguests', '0002_auto_20201105_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guest',
            options={'permissions': [('can_add_guest', 'Может добавлять гостя'), ('can_change_guest', 'Может изменять гостя'), ('can_delete_guest', 'Может удалять гостя'), ('can_view_guest', 'Может просматривать гостя')], 'verbose_name': 'Гость', 'verbose_name_plural': 'Гости'},
        ),
    ]
