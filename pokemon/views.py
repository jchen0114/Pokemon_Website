from django.shortcuts import render

# Create your views here.
from .models import Pokemon, Attack, Type, Movie, Generation, Region

def index(request):
    pokemon_list = Pokemon.objects.all()
    context = {'pokemons:pokemon_list': 'pokemons:pokemon_list'}
    return render(request, 'pokemon/names.html', context = context)

from .forms import PokemonForm, RawPokemonForm, PokemonModelForm

def pokemon_create_view(request):
    form = RawPokemonForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        n = form.cleaned_data.get('pokemon_name')
        t = form.cleaned_data.get('types')
        instance = Pokemon.objects.create(pokemon_name=n)
        for i in t:
            instance.types.add(i)
        form = RawPokemonForm()
    context = {
        'form' : form
    }
    return render(request, "pokemon/pokemon_create.html", context=context)

from django.shortcuts import get_object_or_404

def singlePokemon(request, id):
    pokemon_list = get_object_or_404(Pokemon, id=id)
    context = {
        'pokemon_list' : pokemon_list
    }
    return render(request, 'pokemon/pokemon_detail.html', context=context)

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .filters import PokemonFilter


class SearchListView(ListView):
    model = Pokemon
    template_name = 'pokemon/search.html'
    strict = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PokemonFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PokemonListView(ListView):
    template_name = 'pokemon/pokemon_list.html'

    def get_queryset(self):
        top = []
        li = ['658','448','778','6','197','700','445','384','282','94','887','248','1','849','249']
        for i in li:
            top.append(get_object_or_404(Pokemon, number=i))
        return top
    
class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokemon/pokemon_detail.html'

class PokemonCreateView(CreateView):
    form_class = PokemonModelForm
    # fields = '__all__'
    template_name = 'pokemon/pokemon_create.html'

class PokemonUpdateView(UpdateView):
    form_class = PokemonModelForm
    template_name = 'pokemon/pokemon_create.html'
    queryset = Pokemon.objects.all()

class MovieListView(ListView):
    model = Movie
    template_name = 'pokemon/movies/movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'pokemon/movies/movie_detail.html'


