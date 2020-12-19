# Generated by Django 2.2.13 on 2020-12-18 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20201218_1647'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('serviceexecutors', '0005_auto_20201210_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductIncomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('qty', models.IntegerField(default=0, verbose_name='Количество')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Товар')),
                ('services_executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceexecutors.ServiceExecutor', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Приход товара',
                'verbose_name_plural': 'Приходы товара',
                'permissions': [('can_add_product_incomes', 'Может приходовать товар'), ('can_change_product_incomes', 'Может изменять приход товара'), ('can_delete_product_incomes', 'Может удалять приход товара'), ('can_view_product_incomes', 'Может просматривать приход товара')],
            },
        ),
    ]