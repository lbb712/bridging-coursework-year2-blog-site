from django.urls import path
from . import views


urlpatterns = [
    path('cvedit', views.cv_edit, name= 'cv_edit'),
    
]