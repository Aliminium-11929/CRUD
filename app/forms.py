from django.forms import ModelForm
from .models import Movie
from django import forms

# Create the form class.
class CreateMovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = [
            'MovieID',
            'MovieTitle',
            'Actor1Name',
            'Actor2Name',
            'DirectorName',
            'MovieGenre',
            'ReleaseYear',
        ]

class MovieForm(forms.Form):
	MovieID = forms.IntegerField()
 
 