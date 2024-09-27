from django.contrib.auth.models import User
from django.db import models

class Household(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='households')