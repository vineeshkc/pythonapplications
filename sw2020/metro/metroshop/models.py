from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date

# Create your models here.
class Master_config(models.Model):

    company_code = models.CharField(primary_key='True', max_length=100)
    company_name = models.CharField(max_length=200)
    company_mobile = models.CharField(max_length=200)
    company_address = models.CharField(max_length=100)

    def __str__(self):
        return self.company_code
