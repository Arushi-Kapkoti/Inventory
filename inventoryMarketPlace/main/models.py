from django.db import models
#importing AbstractUser class so that we can inherit from it
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    aadhar = models.PositiveIntegerField(null = True, blank = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField(null = True, blank = True)