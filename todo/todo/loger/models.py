from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title