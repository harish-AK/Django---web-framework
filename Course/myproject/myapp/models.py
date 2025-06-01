from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} {self.phone} {self.time}"