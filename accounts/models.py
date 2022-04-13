from django.db import models
from datetime import datetime

# Create your models here.
class Contractors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    pay_rate = models.DecimalField(max_digits=8, decimal_places=2)
    bill_rate = models.DecimalField(max_digits=8, decimal_places=2)
    startdate = models.DateField(default=datetime.now)
    enddate =  models.DateField(default=datetime.now)


    

