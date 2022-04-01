from django.db import models

# Create your models here.

class todoDataSet(models.Model):
    name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=6,decimal_places=3)
    address = models.TextField()

    def __str__(self):
        return self.name
