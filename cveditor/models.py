from django.db import models
    
class CV(models.Model):
    pass
    
class Item(models.Model):
    text = models.TextField(default='')
    cv =  models.ForeignKey(CV, default=None, on_delete=models.CASCADE)