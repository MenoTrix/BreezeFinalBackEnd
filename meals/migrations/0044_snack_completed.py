# Generated by Django 3.2.14 on 2022-08-21 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0043_chicken_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
