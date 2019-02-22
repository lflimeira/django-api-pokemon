from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    age = models.DateField()

    def __str__(self):
        return self.name
