# Generated by Django 2.1.2 on 2019-01-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0023_auto_20190110_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing'), ('shipping', 'Shipping address'), ('billing', 'Billing address')], max_length=120),
        ),
    ]