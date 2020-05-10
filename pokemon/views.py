from django.shortcuts import render
from .models import Pokemon, Attack, Type, Movie, Generation, Region, Blog
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
from django.views.generic import (ListView, DetailView, CreateView, 
                                    UpdateView, TemplateView)
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
    
    def get(self, request):
        context = {}
        query = ''
        top = []
        li = ['658','448','778','6','197','700','445','384','282','94','887','248','1','849','249']
        for i in li:
            top.append(get_object_or_404(Pokemon, number=i))

        context['pokemon'] = top
        if request.GET:
            query = request.GET.get('q','')
            context['query'] = str(query)
            pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
            context['pokemon_name'] = pokemon_name
        return render(request, self.template_name, context)


class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokemon/pokemon_detail.html'

    def get(self, request, pk):
        context = {}
        query = ''

        if request.GET:
            query = request.GET.get('q','')
            context['query'] = str(query)
            pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
            context['pokemon_name'] = pokemon_name
        context['pokemon'] = Pokemon.objects.all()[pk-1]
        return render(request, self.template_name, context)

class PokemonCreateView(CreateView):
    form_class = PokemonModelForm
    template_name = 'pokemon/pokemon_create.html'

class PokemonUpdateView(UpdateView):
    form_class = PokemonModelForm
    template_name = 'pokemon/pokemon_create.html'
    queryset = Pokemon.objects.all()

class MovieListView(ListView):
    model = Movie
    # queryset = Movie.objects.all()
    template_name = 'movies/movie_list.html'
    
    def get(self, request):
        context = {}
        query = ''
        if request.GET:
            query = request.GET.get('q','')
            context['query'] = str(query)
            pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
            context['pokemon_name'] = pokemon_name
        context['movies'] = Movie.objects.all()
        return render(request, self.template_name, context)

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

    def get(self, request, pk):
        context = {}
        query = ''

        if request.GET:
            query = request.GET.get('q','')
            context['query'] = str(query)
            pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
            context['pokemon_name'] = pokemon_name
        context['movie'] = Movie.objects.all()[pk-1]
        return render(request, self.template_name, context)

class TypeListView(ListView):
    # model = Type
    template_name = 'pokemon/typechart.html'

    def get(self, request):
        context = {}
        query = ''
        if request.GET:
            query = request.GET.get('q','')
            context['query'] = str(query)
            pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
            context['pokemon_name'] = pokemon_name
        # context['types'] = Type.objects.all()

        return render(request, self.template_name, context)


class BlogListView(ListView):
    queryset = Blog.objects.all().order_by('-id')
    template_name = 'blog/blog_list.html'

class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'

    def get(self, request, pk):
        context = {}
        query = ''

        if request.GET:
            query = request.GET.get('q','')
            context['query'] = str(query)
            pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
            context['pokemon_name'] = pokemon_name
        context['blog'] = Blog.objects.all()[pk-1]
        return render(request, self.template_name, context)
        

from django.db.models import Q
from operator import attrgetter
# class HomeView(ListView):
#     model = Pokemon
#     template_name = 'home.html'

#     def get(self, request):
#         context = {}
#         query = ''
#         if request.GET:
#             query = request.GET.get('q','')
#             context['query'] = str(query)
#             pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
#             context['pokemon_name'] = pokemon_name

#         return render(request, self.template_name, context)

#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         context['blogs'] = BlogPost.objects.all()
        
#         return context


def home_screen_view(request):
    query = ""
    context = {}

    if request.GET:
        query = request.GET.get('q','')
        context['query'] = str(query)
        pokemon_name = sorted(get_pokemon_queryset(query), key=attrgetter('number'))
        context['pokemon_name'] = pokemon_name
    
    context['blogs'] = Blog.objects.all().order_by('id')

    return render(request, "home.html", context)


def get_pokemon_queryset(query=None):
    queryset = []
    queries = query.split(" ") # python install 2019 = [python, install, 2019]
    for q in queries:
        if q.isdigit():
            pokemons = Pokemon.objects.filter(
            Q(number=q)).distinct()
            for p in pokemons:
                queryset.append(p)
        else:
            pokemons = Pokemon.objects.filter(
                Q(pokemon_name__icontains=q)).distinct()
            for p in pokemons:
                queryset.append(p)        

    return list(set(queryset))

class IntroView(ListView):
    model = Blog
    template_name = 'pre-home.html'
