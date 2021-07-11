from django.db import models


class Account(models.Model):
    # ForeignKey means many-to-one relationship, in this scenario, many Accounts to one user
    user_id = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL)
    card_number = models.CharField(max_length=30, primary_key=True, unique=True)
    balance = models.IntegerField(default=0)
