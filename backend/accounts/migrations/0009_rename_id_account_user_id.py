# Generated by Django 3.2.5 on 2021-07-11 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_owner_account_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='id',
            new_name='user_id',
        ),
    ]