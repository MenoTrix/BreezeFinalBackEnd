# Generated by Django 3.2.14 on 2022-08-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0044_snack_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakeries',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='breakfast_meals',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fruit',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='meat',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supplements',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vegetables',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
