from django.urls import path
from . import views


urlpatterns = [
    path('cvedit', views.cv_edit, name= 'cv_edit'),
    path('cvedit/the_only_CV_in_the_world/', views.view_cv, name='view_cv'),
    path('cvedit/new', views.new_cv, name='new_cv'),
]