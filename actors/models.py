from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (
    ('US', 'United States'),   
    ('UK', 'United Kingdom'),
    ('FR', 'France'),
    ('JP', 'Japan'),
    ('IN', 'India'),
    ('BR', 'Brazil'),
    ('CN', 'China'),
    ('DE', 'Germany'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('KR', 'Korea')
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    Nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, default='US')
    
    def __str__(self):
        return self.name