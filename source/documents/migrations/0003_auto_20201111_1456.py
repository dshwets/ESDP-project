# Generated by Django 2.2.13 on 2020-11-11 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20201104_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'permissions': [('can_add_document', 'Может добавлять документ'), ('can_change_document', 'Может изменять документ'), ('can_delete_document', 'Может удалять документ'), ('can_view_document', 'Может просматривать документ')], 'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.RenameField(
            model_name='document',
            old_name='pic',
            new_name='file',
        ),
    ]