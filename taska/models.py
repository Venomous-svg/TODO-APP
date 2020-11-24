from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.
class items(models.Model):
    TEXT=models.TextField()
    



    def get_absolute_url(self):
        return reverse('sarasu')
    def __str__(self):
        return self.TEXT    

