# Generated by Django 2.1.2 on 2019-01-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0022_auto_20190110_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping address'), ('shipping', 'Shipping'), ('billing', 'Billing address'), ('billing', 'Billing')], max_length=120),
        ),
    ]