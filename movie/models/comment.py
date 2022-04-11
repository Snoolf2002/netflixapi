from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()  # Djangoning auth va permission uchun User modelini o'zgartirish uchun get_user_model dan foydalanildi


class Comment(models.Model):
    movie_id        = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    text            = models.CharField(max_length=512)
    created_date    = models.DateTimeField(auto_now_add=True)