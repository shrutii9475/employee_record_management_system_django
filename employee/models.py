from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# After adding or modifying the model, you need to create a new migration and apply it to your database. In your terminal or command prompt, run:

# python manage.py makemigrations
# python manage.py migrate

class EmployeeDetail(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null=True)
    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    coursepg = models.CharField(max_length=100,  null=True)
    schoolclgpg = models.CharField(max_length=200, null=True)
    yearofpassingpg = models.CharField(max_length=20, null=True)
    percentagepg = models.CharField(max_length=20, null=True)

    courseug = models.CharField(max_length=100,  null=True)
    schoolclgug = models.CharField(max_length=200, null=True)
    yearofpassingug = models.CharField(max_length=20, null=True)
    percentageug = models.CharField(max_length=20, null=True)

    coursessc = models.CharField(max_length=100,  null=True)
    schoolclgssc = models.CharField(max_length=200, null=True)
    yearofpassingssc = models.CharField(max_length=20, null=True)
    percentagessc = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    c1name = models.CharField(max_length=100,  null=True)
    c1designation = models.CharField(max_length=100,  null=True)
    c1salary = models.CharField(max_length=100,  null=True)
    c1duration = models.CharField(max_length=100,  null=True)

    c2name = models.CharField(max_length=100,  null=True)
    c2designation = models.CharField(max_length=100,  null=True)
    c2salary = models.CharField(max_length=100,  null=True)
    c2duration = models.CharField(max_length=100,  null=True)

    c3name = models.CharField(max_length=100,  null=True)
    c3designation = models.CharField(max_length=100,  null=True)
    c3salary = models.CharField(max_length=100,  null=True)
    c3duration = models.CharField(max_length=100,  null=True)

    def __str__(self):
        return self.user.username