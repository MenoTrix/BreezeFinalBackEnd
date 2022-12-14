# Generated by Django 3.2.14 on 2022-08-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0039_alter_addedmeal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddNewMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10000)),
                ('body', models.CharField(blank=True, max_length=10000)),
                ('image', models.CharField(blank=True, max_length=2000)),
                ('price', models.FloatField(blank=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
