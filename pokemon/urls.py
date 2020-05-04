"""prjoect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'pokemons'
urlpatterns = [
    path('top_pokemons/', views.PokemonListView.as_view(), name='pokemon'),
    path('create/', views.PokemonCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PokemonDetailView.as_view(), name='pokemon_id'),
    path('<int:pk>/update/', views.PokemonUpdateView.as_view(), name='update'),
    path('movie/', views.MovieListView.as_view(), name='movie'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_id'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('type/', views.TypeListView.as_view(), name='type'),
    path('test/', views.TestFilterView.as_view(), name='test')
]

