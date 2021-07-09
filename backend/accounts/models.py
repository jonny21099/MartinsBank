from django.db import models

# Create your models here.
class Accounts(models.Model):
    title = model.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title