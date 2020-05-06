from django import forms
from .models import Pokemon, Attack, Type, BlogPost

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'

class RawPokemonForm(forms.Form):
    pokemon_name = forms.CharField()
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all())

class PokemonModelForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'pokemon_name' : 'pokemon_name',
            'number': 'number',
            'types': 'types',
        }

