# Generated by Django 4.0.5 on 2022-06-26 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='state',
        ),
    ]