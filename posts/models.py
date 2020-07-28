from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user_model = get_user_model()

class UserPost(models.Model):
    date = models.DateField()
    text = models.TextField()
    users = models.ForeignKey(user_model, on_delete=models.CASCADE)
