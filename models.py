from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    #pict = models.ImageField(upload_to='/media/', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return    self.title



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
