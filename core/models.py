from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_branch = models.BooleanField('Is customer', default=False)

class Banglore(models.Model):
    date = models.DateField()
    line1 = models.IntegerField()
    line2 = models.IntegerField()
    line3 = models.IntegerField()
    line4 = models.IntegerField()
    line5 = models.IntegerField()



class Mumbai(models.Model):
    date = models.DateField()
    line1 = models.IntegerField()
    line2 = models.IntegerField()
    line3 = models.IntegerField()

    
   

class Chennai(models.Model):
    date = models.DateField()
    line1 = models.IntegerField()
    line2 = models.IntegerField()
    line3 = models.IntegerField()
    line4 = models.IntegerField()

   