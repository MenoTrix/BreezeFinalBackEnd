# Generated by Django 3.2.14 on 2022-08-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0040_addnewmeal'),
    ]

    operations = [
        migrations.AddField(
            model_name='keto',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
