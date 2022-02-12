from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender=models.CharField(max_length=6, choices=[('male','Male'),('female','Female')],default='Male')
