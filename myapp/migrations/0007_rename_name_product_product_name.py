# Generated by Django 4.2 on 2024-12-10 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
