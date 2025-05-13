from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name