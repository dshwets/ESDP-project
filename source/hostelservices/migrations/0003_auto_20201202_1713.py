# Generated by Django 2.2.13 on 2020-12-02 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostelservices', '0002_auto_20201110_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostelservice',
            old_name='name',
            new_name='service_name',
        ),
        migrations.RemoveField(
            model_name='hostelservice',
            name='price',
        ),
        migrations.CreateModel(
            name='SellingPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена продажи')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
            ],
            options={
                'verbose_name': 'Цена продажи',
                'verbose_name_plural': 'Цены продажи',
                'permissions': [('can_add_selling_price', 'Может добавлять цену продажи'), ('can_change_selling_price', 'Может изменять цену продажи'), ('can_delete_selling_price', 'Может удалять цену продажи'), ('can_view_selling_price', 'Может просматривать цену продажи')],
            },
        ),
        migrations.CreateModel(
            name='PurchasePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена продажи')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
            ],
            options={
                'verbose_name': 'Цена покупки',
                'verbose_name_plural': 'Цены покупки',
                'permissions': [('can_add_purchase_price', 'Может добавлять цену покупки'), ('can_change_purchase_price', 'Может изменять цену покупки'), ('can_delete_purchase_price', 'Может удалять цену покупки'), ('can_view_purchase_price', 'Может просматривать цену покупки')],
            },
        ),
    ]