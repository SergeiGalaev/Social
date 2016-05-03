from django.db import models
from django.utils import timezone



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bdate = models.DateField(blank=True, null=True)
    adress = models.CharField(max_length=100)
    
    
class Parents(models.Model):
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_place = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    adress = models.CharField(max_length=100)
