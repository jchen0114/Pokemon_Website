from django.db import models
from django.urls import reverse

# Create your models here.

class Type(models.Model):
    types = models.CharField(max_length=10)
    
    def __str__(self):
        return self.types

class Region(models.Model):
    region = models.CharField(max_length=10, default=None)
    def __str__(self):
        return self.region

class Generation(models.Model):
    generation = models.CharField(max_length=15, default=None)
    def __str__(self):
        return self.generation

class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length = 20)
    types = models.ManyToManyField(Type)
    number = models.IntegerField()
    rank = models.IntegerField()
    image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)
    type_idx = models.IntegerField()
    type_idx2 = models.IntegerField()
    lower_evolve = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='low')
    upper_evolve = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='up')
    levelup = models.IntegerField()
    special_case = models.TextField(max_length = 100, blank=True)
    evolve_tool = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',blank=True)
    summary = models.TextField(max_length=500, blank=True)
    weakness = models.ManyToManyField(Type, related_name='weakness')
    evolve_img = models.ImageField(upload_to='image/evolve',default=u'image/default.png',blank=True)
    evolve_kinds = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)


    def __str__(self):
        return self.pokemon_name

    def get_absolute_url(self):
        return reverse("pokemons:pokemon_id", kwargs={"pk": self.pk})


class Attack(models.Model):
    attack_name = models.CharField(max_length = 30)
    damage = models.DecimalField(max_digits = 3, decimal_places = 0)
    types = models.ManyToManyField(Type)

    def __str__(self):
        return f'{self.attack_name, self.damage}'
    
    def get_absolute_url(self):
        return reverse("pokemons:attack_id", kwargs={"pk": self.pk})

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release = models.DateField(null=True, blank=True)
    summary = models.TextField(max_length=1000)
    number = models.IntegerField()
    pokemon = models.ManyToManyField(Pokemon)
    image = models.ImageField(upload_to='movies/%Y/%m',max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pokemons:movie", kwargs={"pk": self.pk})

from django.contrib import admin

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'pokemon_name', 'number', 'region']
    serach_fields = ('pokemon_name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Type._meta.fields]

@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Attack._meta.fields]
    list_filter = ('types',)
    serach_fields = ('damage','attack_name')
    ordering = ('damage',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'title']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'region']

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'generation']