# Generated by Django 3.2.5 on 2021-07-11 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210711_0737'),
        ('accounts', '0012_alter_account_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]