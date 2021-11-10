from django.db import models
from django.utils import timezone


class Job_Upload(models.Model):
    Designation = models.CharField(max_length = 250)
    Location    = models.CharField(max_length = 250)
    Client_Name = models.CharField(max_length = 250)
    Functional_Area = models.CharField(max_length = 250)
    Industry    = models.CharField(max_length = 250)
    Experience  = models.CharField(max_length = 250)
    Job_Description = models.TextField()
    Rate_Card   = models.CharField(max_length = 250)
    Salary_LPA  = models.CharField(max_length = 250)
    Notice_Period = models.CharField(max_length = 250)
    Posted_On    = models.DateTimeField(default=timezone.now)
    
    