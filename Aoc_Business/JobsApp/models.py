from django.db import models
from django.utils import timezone
import datetime

class Job_Upload(models.Model):
    Designation = models.CharField(max_length = 250)
    Education   = models.CharField(max_length = 250,default = 'UG/PG')
    Location    = models.CharField(max_length = 250)
    Client_Name = models.CharField(max_length = 250)
    Functional_Area = models.CharField(max_length = 250)
    Industry    = models.CharField(max_length = 250)
    Experience  = models.CharField(max_length = 250)
    Job_Description = models.TextField()
    Job_Description1 = models.TextField(default='')
    Job_Description2 = models.TextField(default='')
    Job_Description3 = models.TextField(default='')
    Rate_Card   = models.CharField(max_length = 250)
    Salary_LPA  = models.CharField(max_length = 250)
    Notice_Period = models.CharField(max_length = 250)
    Openings    = models.CharField(max_length = 250,default=1)
    Role        = models.CharField(max_length = 250,default='')
    Freelancing = models.CharField(max_length = 250,default='No')
    Posted_On    = models.DateTimeField(default=timezone.now)
    
   