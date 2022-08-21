# Generated by Django 4.1 on 2022-08-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0020_bakeries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='category',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='bakeries',
            name='contain',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='bakeries',
            name='image',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='bakeries',
            name='ingredient',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='bakeries',
            name='storing',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='bakeries',
            name='weight',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]