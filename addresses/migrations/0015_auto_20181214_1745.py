# Generated by Django 2.1.2 on 2018-12-14 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0014_auto_20181214_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]
