from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    level = models.CharField(max_length=50, choices=[
        ('jun', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior')
    ], null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
