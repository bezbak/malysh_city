# Generated by Django 4.1.5 on 2023-01-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Media',
        ),
    ]
