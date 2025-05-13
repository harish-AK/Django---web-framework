from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) # unique emails
    def __str__(self): # to display the message in readable form
        return self.username