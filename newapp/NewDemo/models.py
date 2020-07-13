from django.db import models
import datetime
class movie_list(models.Model):
    movie_name = models.CharField(max_length=500)
    release_date = models.CharField(max_length=500)
    def __str__(self):
        return self.movie_name

class details(models.Model):
    movie = models.ForeignKey(movie_list,on_delete=models.CASCADE)
    movie_budget = models.CharField(max_length=500)
    movie_revenue = models.CharField(max_length=500)
    movie_review = models.CharField(max_length=500)
    def __str__(self):
       return str(self.movie_budget)
