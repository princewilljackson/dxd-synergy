# Generated by Django 4.0.5 on 2022-07-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='0000', editable=False, max_length=32),
        ),
    ]
