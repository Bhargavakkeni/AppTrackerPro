from django.db import models

# Create your models here.

class LoginDetails(models.Model):
    username = models.CharField(max_length = 255, primary_key = True)
    password = models.CharField(max_length = 155)

class AppDetails(models.Model):
    icons = models.ImageField(upload_to='images/')
    appName = models.CharField(max_length = 200)
    appLink = models.URLField()
    category = models.CharField(max_length = 255)
    subCategory = models.CharField(max_length = 255)
    points = models.IntegerField()