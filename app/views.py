from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import CreateMovieForm, MovieForm
from .models import Movie


def index(request):
	return render(request,'index.html')

def add_movie(request):
	if request.method == 'POST':
		form = CreateMovieForm(request.POST)
		if form.is_valid():
			Movieform = form.cleaned_data
			ID = Movieform['MovieID']
			MovieTitle = Movieform['MovieTitle']
			Actor1Name = Movieform['Actor1Name']
			Actor2Name = Movieform['Actor2Name']
			DirectorName = Movieform['DirectorName']
			MovieGenre = Movieform['MovieGenre']
			ReleaseYear = Movieform['ReleaseYear']
			Movie.objects.create(
                MovieID=ID, 
                MovieTitle=MovieTitle,
                Actor1Name=Actor1Name,
                Actor2Name=Actor2Name,
                DirectorName=DirectorName,
                MovieGenre=MovieGenre,
                ReleaseYear=ReleaseYear
            )
			return render(request, 'index.html')
	else:
		form = CreateMovieForm()
	M=Movie.objects.all()
	return render(request, 'add_movie.html', {'form': form,'M':M})

def movie_info(request):
	if request.method == 'POST':
		form = MovieForm(request.POST)

		if form.is_valid():
			movieform = form.cleaned_data
			MovieID = movieform['MovieID']
						
			for e in Movie.objects.all():
				if e.MovieID==MovieID:
					movie=e
			return render(request, 'movie_info.html', { 'form': form,'movie':movie})
		
	else:
		form= MovieForm()
	return render(request,'movie_info.html',{'form':form})

def delete(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        
        if form.is_valid():
            movieform = form.cleaned_data
            MovieID = movieform['MovieID']
            
            for e in Movie.objects.all():
                if e.MovieID==MovieID:
                    movie = Movie(
                        MovieID=e.MovieID,
                        MovieTitle=e.MovieTitle,
                        Actor1Name=e.Actor1Name,
                        Actor2Name=e.Actor2Name,
                        DirectorName=e.DirectorName,
                        MovieGenre=e.MovieGenre,
                        ReleaseYear=e.ReleaseYear
                    )
                    e.delete()
            return render(request, 'delete_movie.html', {'form': form,'movie':movie,'message': "The above movie has been deleted successfully."})
    else:
        form= MovieForm()
        return render(request,'delete_movie.html',{'form':form})
    
    
def update(request):
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)
        
        # Extract data directly from POST since form validation fails due to uniqueness constraint
        movieform = request.POST
        MovieID = movieform.get('MovieID')
        MovieTitle = movieform.get('MovieTitle')
        Actor1Name = movieform.get('Actor1Name')
        Actor2Name = movieform.get('Actor2Name')
        DirectorName = movieform.get('DirectorName')
        MovieGenre = movieform.get('MovieGenre')
        ReleaseYear = movieform.get('ReleaseYear')
        
        # Check if all required fields are provided
        if all([MovieID, MovieTitle, Actor1Name, Actor2Name, DirectorName, MovieGenre, ReleaseYear]):
            try:
                # Find the movie to update (strict update - no create)
                movie = Movie.objects.get(MovieID=MovieID)
                
                # Update the movie fields
                movie.MovieTitle = MovieTitle
                movie.Actor1Name = Actor1Name
                movie.Actor2Name = Actor2Name
                movie.DirectorName = DirectorName
                movie.MovieGenre = MovieGenre
                movie.ReleaseYear = ReleaseYear
                
                # Save the changes
                movie.save()
                
                print(f"Movie updated: {movie.MovieTitle}")
                
                return render(request, 'update_movie.html', {
                    'form': form, 
                    'movie': movie, 
                    'message': "Movie updated successfully!"
                })
                
            except Movie.DoesNotExist:
                return render(request, 'update_movie.html', {
                    'form': form, 
                    'error': f"Movie with ID '{MovieID}' does not exist. Please check the Movie ID and try again."
                })
            except Exception as e:
                print(f"Error updating movie: {e}")
                return render(request, 'update_movie.html', {
                    'form': form, 
                    'error': f"Error updating movie: {str(e)}"
                })
        else:
            return render(request, 'update_movie.html', {
                'form': form, 
                'error': "Please fill in all required fields."
            })
    else:
        form = CreateMovieForm()
    
    M = Movie.objects.all()
    return render(request, 'update_movie.html', {'form': form, 'M': M})