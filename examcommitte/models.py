from django.db import models

# Create your models here.
from django.db import models
class User:
    username = models.CharField()
    pass1 = models.TextField(max_length=255)
    email = models.EmailField()

class teacher(models.Model):
    teacherID = models.CharField(max_length=25,null=True,default='1')
    userName =  models.CharField(max_length=25)
    firstName =  models.CharField(max_length=25)
    lastName =  models.CharField(max_length=25)
    email =  models.CharField(max_length=25)
    password =  models.CharField(max_length=25)
    isCommittee = models.CharField(max_length=25)
    isHeadOfCommittee= models.CharField(max_length=25)
    def __str__(self):
     return f'{self.userName}'
 
class student(models.Model):
    year = models.IntegerField()
    numberOfStudent =  models.IntegerField()
    def __str__(self):
     return f'{self.year}'