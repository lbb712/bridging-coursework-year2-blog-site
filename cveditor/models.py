from django.db import models
from django.utils import timezone 

    
class CV(models.Model):
    title = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField(default= timezone.now)
    name = models.CharField(max_length=200, default='')
    address_line_1 = models.CharField(max_length=200, default='')
    address_line_2 = models.CharField(max_length=200, default='')
    address_line_3 = models.CharField(max_length=200, default='', blank=True)
    town = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=12, null=True, blank=True, default=None)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    
    personal_profile = models.TextField(blank=True)
    
    university_name = models.CharField(max_length=200, blank=True, default='')
    modules_studied = models.TextField(blank=True)
    sixth_form_or_college_name = models.CharField(max_length=200, blank=True, default='')
    alevel_results = models.TextField(blank=True)
    school_name = models.CharField(max_length=200, blank=True, default='')
    gcse_results = models.TextField(blank=True)
    
    experience = models.TextField(blank=True)
    employment = models.TextField(blank=True)
    
    skills_and_achievements = models.TextField(blank=True)
    
    academic_referee = models.CharField(max_length=200, blank=True, default='')
    academic_referee_contact_details = models.TextField(blank=True)
    employment_referee = models.CharField(max_length=200, blank=True, default='')
    employment_referee_contact_details = models.TextField(blank=True)