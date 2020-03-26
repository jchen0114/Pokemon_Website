import django_filters
from .models import Pokemon, Type
from django import forms

class PokemonFilter(django_filters.FilterSet):

    CHOICES = {
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    }

    pokemon_name = django_filters.CharFilter(lookup_expr='icontains', label='Pokemon Name')
    number = django_filters.CharFilter(label='Pokemon Number')
    ordering = django_filters.ChoiceFilter(choices=CHOICES, method='filter_by_ordering', label='Ordering')
    types = django_filters.ModelMultipleChoiceFilter(queryset=Type.objects.all())
    class Meta:
        model = Pokemon
        fields = ['pokemon_name', 'number', 'types']

    def filter_by_ordering(self, queryset, name, value):
        expression = 'number' if value =='ascending' else '-number'
        return queryset.order_by(expression)

    def __init__(self, *args, **kwargs):
        super(PokemonFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()



class IndexFilter(django_filters.FilterSet):

    class Meta:
        model = Pokemon
        fields = ['pokemon_name']

    def __init__(self, *args, **kwargs):
        super(PokemonFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()