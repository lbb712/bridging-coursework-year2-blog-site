from django.urls import path
from . import views


urlpatterns = [
    path('cvedit/<int:pk>/edit/', views.cv_edit, name= 'cv_edit'),
    path('cvedit/<int:pk>/', views.view_cv, name='view_cv'),
    path('cvedit/new/', views.new_cv, name='new_cv'),
    path('cvedit/list', views.cv_list, name='cv_list'),
    path('cvedit/<pk>/remove/', views.cv_remove, name='remove_cv'),
]