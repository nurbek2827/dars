from django.db import models


# Create your models here.

class Ishchi(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=128)
    gender = models.BooleanField(default=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=50)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.name
