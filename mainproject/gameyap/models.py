from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
