from django.urls import re_path, path, include

#from django.conf.urls import url
from . import views


urlpatterns = [
    path('',views.index),
    path('add_movie/',views.add_movie),
    path('movie_info/',views.movie_info),
    path('delete_movie/',views.delete),
    path('update_movie/',views.update),
]
