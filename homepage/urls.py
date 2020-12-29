from django.urls import path
from . import views
app_name = 'homepage'

urlpatterns = [
    path('', views.homepage),
    path('projects/', views.project, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('notFound/', views.notFound, name='notFound'),
    path('skill/', views.skill, name='skill'),
]
