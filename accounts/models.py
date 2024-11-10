from django.db import models
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class user_data(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    phn_no = models.BigIntegerField()
    gender = models.CharField()
    salary = models.IntegerField()
    address = models.CharField(max_length=40)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    is_anonymous = False
    is_authenticated = True