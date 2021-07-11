# Generated by Django 3.2.5 on 2021-07-11 13:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_account_card_number'),
        ('users', '0007_rename_test_card_number_user_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account', unique=True, verbose_name='Card Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
