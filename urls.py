from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('project', views.project, name="project"),
    path('experience', views.experience, name="experience"),
    path('project1', views.project1, name="project1"),
    path('project2', views.project2, name="project2"),
    path('project3', views.project3, name="project3"),
]