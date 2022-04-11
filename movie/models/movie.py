from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    imdb = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    actors = models.ManyToManyField('Actor')
    
    def __str__(self):
        return self.title