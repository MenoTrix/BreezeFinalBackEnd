# Generated by Django 4.1 on 2022-08-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0022_vegan'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplements',
            name='Flavor',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
