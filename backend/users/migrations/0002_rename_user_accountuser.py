# Generated by Django 3.2.5 on 2021-07-10 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210710_1431'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AccountUser',
        ),
    ]