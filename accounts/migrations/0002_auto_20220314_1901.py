# Generated by Django 3.1 on 2022-03-14 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='firt_name',
            new_name='first_name',
        ),
    ]
