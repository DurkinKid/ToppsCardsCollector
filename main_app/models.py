from django.db import models
from django.urls import reverse

class Topp(models.Model):  
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    highlight = models.TextField(max_length=250)
    year = models.IntegerField()
    company = models.CharField(max_length=100)
    img = models.URLField(max_length=500)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'topp_id': self.id})


class Joke(models.Model):
    joke = models.TextField(max_length=150)
    