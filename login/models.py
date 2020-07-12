from django.db import models

# Create your models here.

class usersLogin(models.Model):
    email = models.CharField(max_length=1)
    password = models.CharField(max_length=100)
