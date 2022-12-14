# Generated by Django 4.0.5 on 2022-08-15 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0013_alter_lowcarb_amount_alter_lowcarb_calories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='meals.category')),
            ],
        ),
        migrations.AlterField(
            model_name='lowcarb',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_lowcarb', to='meals.category_lowcarb'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('body', models.CharField(blank=True, max_length=10000)),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('brandUrl', models.CharField(blank=True, max_length=200)),
                ('calories', models.FloatField()),
                ('cooking', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
                ('nutrition', models.CharField(blank=True, max_length=200)),
                ('price', models.FloatField()),
                ('sale', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('weight', models.CharField(blank=True, max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category1', to='meals.category_type')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='meals.category')),
            ],
        ),
    ]
