from django.db import models
from django.utils import timezone 
    
class CV(models.Model):
    title = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField(default= timezone.now)
    name = models.CharField(max_length=200, default='')