# Generated by Django 2.1.2 on 2019-01-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0019_auto_20190109_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing')], max_length=120),
        ),
    ]
