# Generated by Django 4.0.5 on 2022-08-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_alter_toparrival_body_alter_toparrival_brandurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topproducts',
            name='body',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='brandUrl',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='cooking',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='ingredient',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='nutrition',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]