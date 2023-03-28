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
 
class course(models.Model):
    courseTitle = models.CharField(max_length=255)
    courseCode = models.CharField(max_length=255)
    courseCredit = models.CharField(max_length=255)
    courseTeacher = models.CharField(max_length=255)
    externalTeacher = models.CharField(max_length=255)
    def __str__(self):
     return f'{self.courseTitle}'
class createdExamCommittee(models.Model):
    examCommitteeYear = models.CharField(max_length=255)
    examCommitteeStatus = models.CharField(max_length =255)
    def __str__(self):
     return f'{self.examCommitteeYear}'
 
class Semister(models.Model):
    semNo=models.IntegerField()
    def __str__(self):
        return f'{self.semNo}'
class routine(models.Model):
    semester=models.CharField(max_length=255)
    courseCode =models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    start=models.TimeField(null=True)
    end=models.TimeField(null=True)
    teachers=models.ManyToManyField(teacher)
    def __str__(self):
        return f'{self.courseCode}'

class teacherCount(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    count = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.firstName}'