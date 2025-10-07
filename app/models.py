from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Movie(models.Model):
    MovieID= models.IntegerField(primary_key=True)
    MovieTitle = models.CharField(max_length=30)
    Actor1Name = models.CharField(max_length=30)
    Actor2Name = models.CharField(max_length=30)
    DirectorName = models.CharField(max_length=30)
    MovieGenre = models.CharField(max_length=30)
    ReleaseYear = models.IntegerField(default=datetime.now().year,
                                      validators=[
                                            MinValueValidator(1888),
                                            MaxValueValidator(datetime.now().year+10)
                                        ]
                                    )