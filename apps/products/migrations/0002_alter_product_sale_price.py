# Generated by Django 4.1.5 on 2023-01-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]