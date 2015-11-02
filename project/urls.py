"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
# from django.conf.urls.defaults import *
# from main.models import Pokemon
# from vote.views import vote_on_object

# def vote_view(request):
    # pokemon_dict = {
    #   'model': Pokemon,
    #   'template_object_name': 'tip',
    #   'slug_field': 'slug',
    #   'allow_xmlhttprequest': 'true',
    # }

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.PokedexListView.as_view(), name='pokedexlist'),
    url(r'^pokedex_detail/(?P<slug>.+)/$', views.PokedexDetailView.as_view(), name='pokedexdetail'),

    url(r'^pokemonlist_view/$', views.PokemonListView.as_view(), name='pokemonlist'),
    url(r'^pokemondetail_view/(?P<slug>.+)/$', views.PokemonDetailView.as_view(), name='pokemondetail'),

    # url(r'^$', views.TypeListView.as_view()),
    # url(r'^Type_detail/(?P<slug>.+)/$', views.TypeDetailView.as_view()),
    
    # url(r'^sprite_view/$', views.SpriteListView.as_view(), name='sprite_view'),
    # url(r'^sprite_detail/(?P<slug>.+)/$', views.SpriteDetailView.as_view(), name='pokedexdetail'),

    # url(r'^(?P<slug>[-\w]+)/(?P<direction>up|down|clear)vote/?$', vote_on_object, pokemon_dict, name="pokemon-voting"),


    url(r'^login_view/$', 'main.views.login_view', name='login_view'),
    url(r'^logout_view/$', 'main.views.logout_view', name='logout_view'),

    url(r'^signup/$', 'main.views.signup', name='signup_view'),

    url(r'^regiser/$', CreateView.as_view(template_name='register.html', form_class=CustomUserCreationForm, success_url='/'))

]
