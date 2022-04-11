from django.db import models


class Actor(models.Model):
    gen = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    name        = models.CharField(max_length=200)
    birthdate   = models.DateField()
    gender      = models.CharField(max_length=50, choices=gen)
    
    def __str__(self):
        return self.name