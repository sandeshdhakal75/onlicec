from django.db import models
from django.contrib.auth.models import User

# Create your models here.



gender = (('male', 'Male'), ('female', 'Female'), ('other', 'Others'))
type = (('Murder','murder'),('Rape','rape'),('Kidnapping','kidnapping'))


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
