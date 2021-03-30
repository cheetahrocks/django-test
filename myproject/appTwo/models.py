from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return self.fname
