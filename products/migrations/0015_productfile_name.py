# Generated by Django 2.1.5 on 2019-01-31 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20190131_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfile',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
