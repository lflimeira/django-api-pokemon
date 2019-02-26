from django.conf import settings
from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    age = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
