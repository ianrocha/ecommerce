# Generated by Django 2.1.5 on 2019-01-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0027_auto_20190130_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('shipping', 'Shipping address'), ('billing', 'Billing'), ('billing', 'Billing address')], max_length=120),
        ),
    ]
