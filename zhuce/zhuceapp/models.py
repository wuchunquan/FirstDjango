from django.db import models
class user(models.Model):
    username = models.CharField(max_length=20)
    userpsw = models.CharField(max_length=20)
    usersmt=models.CharField(max_length=20)
# Create your models here.
