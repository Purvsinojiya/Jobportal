from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from datetime import timedelta, datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Intership = 'Intership'
    
    
class Education(models.TextChoices):
    Bachelors='Bachelors'
    Masters='Masters'
    Phd = 'Phd'
   
class Industry(models.TextChoices):
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education/Training'
    Telecommunication = 'Telecommunication'
    Others = 'Others'
    
class Experience(models.TextChoices):
    No_EXPERIENCE = 'No Experience'
    ONE_YEAR='1 year'
    TWO_YEAR='2 years'
    THREE_YEAR_PLUS='3 years above'  
    
def return_date_time():
    now=datetime.now()
    return now + timedelta(days=10)
    
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200,null=True)
    description =models.TextField(null=True)
    email =models.EmailField(null=True)
    address =models.CharField(max_length=100,null=True)
    jobType = models.CharField(
    
        max_length=10,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
    
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models.CharField(
    
        max_length=30,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
    
        max_length=20,
        choices=Experience.choices,
        default=Experience.No_EXPERIENCE
    )
    salary = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(1000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100,null=True)
    lastDate = models.DateField(default=return_date_time)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
