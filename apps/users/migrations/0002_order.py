# Generated by Django 4.1.5 on 2023-01-07 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_delete_media'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=25)),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Обговор', 'Обговор'), ('Доставка', 'Доставка'), ('Доставлено', 'Доставлено'), ('Возвращено', 'Возвращено'), ('Поменяли', 'Поменяли')], default='Обговор', max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='products.product')),
                ('swipe_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_swipe', to='products.product')),
            ],
        ),
    ]
