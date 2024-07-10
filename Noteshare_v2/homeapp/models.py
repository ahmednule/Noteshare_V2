from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    proffesion = models.CharField(max_length=255)
    instituion = models.CharField(max_length=255)

    """class Meta: 
        db_table = 'User_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    """
