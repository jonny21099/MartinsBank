# Generated by Django 3.2.5 on 2021-07-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_test_card_number_user_card_number'),
        ('accounts', '0010_remove_account_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]
