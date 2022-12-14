# Generated by Django 4.1 on 2022-08-14 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0012_category_lowcarb_lowcarb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lowcarb',
            name='amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='lowcarb',
            name='calories',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='lowcarb',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_lowcarb', to='meals.category_lowcarb'),
        ),
        migrations.AlterField(
            model_name='lowcarb',
            name='image',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='lowcarb',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='lowcarb',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
