from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('<int:movie_id>/',views.details,name='details'),
    path('', views.movie, name='Title'),

]
