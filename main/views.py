from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from main.models import CustomUser
from django.template import RequestContext
from django.db import IntegrityError
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect, HttpResponse

from main.models import Pokemon, Type, Pokedex, Move
from main.models import Ability, Description, Sprite 
from main.forms import UserSingUp, UserLogin

# Create your views here.


class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokemonlist_view.html'


class PokemonDetailView(DetailView):
    model = Pokemon
    slug_field = 'slug'
    template_name = 'pokemondetail_view.html'


class PokedexListView(ListView):
    model = Pokedex
    template_name = 'pokedex_view.html'


class PokedexDetailView(DetailView):
    model = Pokedex
    slug_field = 'slug'
    template_name = 'pokedexdetail.html'


class DescriptionListView(ListView):
    model = Description
    template_name = 'description_list.html'


class DescriptionDetailView(DetailView):
    model = Description
    slug_field = ''
    template_name = 'description_detail.html'


class TypeListView(ListView):
    model = Type
    template_name = 'type_list.html'


class TypeDetailView(DetailView):
    model = Type
    slug_field = ''
    template_name = 'type_detail.html'


class AbilityListView(ListView):
    model = Ability
    template_name = 'ability_list.html'


class AbilityDetailView(DetailView):
    model = Type
    slug_field = ''
    template_name = 'Ablity_detail.html'


class SpriteListView(ListView):
    model = Sprite
    template_name = 'sprite_list.html'


class SpriteDetailView(DetailView):
    model = Sprite
    slug_field = ''
    template_name = 'sprite_detail.html'


class MoveListView(ListView):
    model = Move
    template_name = 'move_list.html'


class MoveDetailView(DetailView):
    model = Move
    slug_field = ''
    template_name = 'move_detail.html'


def signup(request):
    context = {}

    form = UserSingUp

    contex['form'] = form

    if request.method == 'POST':
        form = UserSingUp(request.POST)
        
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleand_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)
                auth_user = authenticate(email=email, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/')

            except IntergrityError, e:
                context['valid'] = "No, Because! No"
        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout(request):
    user_logout(request)

    return HttpResponseRedirect('/')


def login(request):
    context = {}

    form = UserLogin()

    context['form'] = form

    print "in login view"

    if request.method == 'POST':

        print "in post"
        form = UserLogin(request.POST)

        print form.errors

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print email
            print password
            auth_user = authenticate(email=email, password=password)
            print auth_user
            if auth_user is not None:
                user_login(request, auth_user)

                print "auth_user is not none"

                return HttpResponseRedirect('/')
            else:
                context['valid'] = "Please enter a User Name"

        else:
            context['valid'] = "Form is not valid."
    return render_to_response('login.html', context, context_instance=RequestContext(request))

