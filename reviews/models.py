from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação minima de 0 estrelas'),
            MaxValueValidator(5, 'Avaliação maxima de 5 estrelas')
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie