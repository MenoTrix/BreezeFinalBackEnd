# Generated by Django 3.2.14 on 2022-08-18 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0029_auto_20220818_0155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addedmeal',
            old_name='password',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='addedmeal',
            old_name='email',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='addedmeal',
            old_name='username',
            new_name='title',
        ),
    ]
