from django.urls import path

from cinema import views

urlpatterns = [
    path("movies/", views.movies, name="movies"),
    path("movies/<int:pk>/", views.detail, name="movie-detail"),
]

app_name = "cinema"
