# Generated by Django 4.1 on 2022-08-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0025_remove_supplements_productdata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('body', models.CharField(blank=True, max_length=10000)),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('calories', models.FloatField()),
                ('category', models.CharField(blank=True, max_length=2000)),
                ('image', models.CharField(max_length=2000)),
                ('price', models.FloatField()),
                ('sale', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=10000)),
                ('weight', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]