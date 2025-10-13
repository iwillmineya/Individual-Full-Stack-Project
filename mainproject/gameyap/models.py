from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Vote(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    VOTE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=7, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'game')
