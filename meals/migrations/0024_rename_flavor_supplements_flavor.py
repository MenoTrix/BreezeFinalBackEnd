# Generated by Django 4.1 on 2022-08-17 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0023_supplements_flavor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplements',
            old_name='Flavor',
            new_name='flavor',
        ),
    ]
