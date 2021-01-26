from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BShop(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    price = models.CharField(max_length=10)
    genre = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    year = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
