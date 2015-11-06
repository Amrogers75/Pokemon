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
from django.contrib.auth import views as auth_views

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

    url(r'^spritelist/$', views.SpriteListView.as_view(), name='spritelist'),
    url(r'^spritedetail/(?P<slug>.+)/$', views.SpriteDetailView.as_view(), name='spritedetail'),

    # url(r'^card/$', views.CardView.as_view(), name='card'),
    # url(r'^Type_detail/(?P<slug>.+)/$', views.TypeDetailView.as_view(), name=typedetail),
    
    # url(r'^(?P<slug>[-\w]+)/(?P<direction>up|down|clear)vote/?$', vote_on_object, pokemon_dict, name="pokemon-voting"),

    url(r'^json_response/$', 'main.views.json_response', name='jsonresponse'),
    url(r'^ajax_view/$', 'main.views.ajax_search', name='ajaxsearch'),

    url(r'^login/$', 'main.views.login', name='login'),
    url(r'^logout/$', 'main.views.logout', name='logout'),

    url(r'^signup/$', 'main.views.signup', name='signup'),

    url(r'^regiser/$', CreateView.as_view(template_name='register.html', form_class=CustomUserCreationForm, success_url='/'))

]
