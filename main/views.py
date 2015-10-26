from django.shortcuts import render, render_to_response

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect, HttpResponse

from main.models import Pokemon
# from main.models import Pokedex, Type, Ability

# from main.forms import UserSingUp, UserLogin

# Create your views here.


class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokemon_list.html'


class PokemonDetailView(DetailView):
    model = Pokemon
    slug_field = 'descriptions'
    template_name = 'pokemon_detail.html'


# class PokedexListView(ListView):
#     model = Pokedex
#     template_name = 'pokedex_list.html'


# class PokedexDetailView(DetailView):
#     model = Pokedex
#     slug_field = ''
#     template_name = 'pokedex_detail.html'


# class TypeListView(ListView):
#     model = Type
#     template_name = 'type_list.html'


# class TypeDetailView(DetailView):
#     model = Type
#     slug_field = ''
#     template_name = 'type_detail.html'


# class AbilityListView(ListView)
#     model = Ability
#     template_name = 'ability_list.html'

# class AbilityDetailView(DetailView):
#     model = Type
#     slug_field = ''
#     template_name = 'Ablity_detail.html'
