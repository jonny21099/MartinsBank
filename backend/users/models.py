import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name
