from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    contact = models.CharField(null=True,blank=True,max_length=40)
    website = models.URLField(null=True,blank=True)
    department_type = models.CharField(max_length=30)
    description = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)






gender = (('male', 'Male'), ('female', 'Female'), ('other', 'Others'))


class Public(models.Model):
    full_name=models.CharField(max_length=100)
    crime_location = models.CharField(max_length=100)
    complain_description=models.CharField(max_length=30)
    date_of_crime=models.DateField(null=True,blank=True)
    time_of_crime=models.TimeField(null=True,blank=True)
    evidence = models.ImageField(upload_to='img/', null=True, blank=True)
    contact_number = models.CharField(max_length=14)
    complaint_type = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=gender)

    def __str__(self):
        return self.full_name

