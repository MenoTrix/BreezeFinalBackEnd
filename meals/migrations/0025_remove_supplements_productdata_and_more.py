# Generated by Django 4.1 on 2022-08-17 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0024_rename_flavor_supplements_flavor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplements',
            name='ProductData',
        ),
        migrations.RemoveField(
            model_name='supplements',
            name='flavor',
        ),
    ]
