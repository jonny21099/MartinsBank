# Generated by Django 3.2.5 on 2021-07-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='card_number',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]