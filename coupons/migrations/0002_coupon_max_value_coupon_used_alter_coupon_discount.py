# Generated by Django 4.0.6 on 2022-07-19 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='max_value',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Coupon Quantity'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='used',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
