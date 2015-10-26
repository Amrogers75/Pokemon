#!/usr/bin/env python
import requests
import os, sys


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import Pokemon

for pokemon in Pokemon.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 200, 'national_id': pokemon.national_id}

    response = requests.get('http://pokeapi.co/api/v1/pokedex/1/', params=param_dict)
# response = requests.get("https://freemusicarchive.org/api/get/genres.json?api_key=LFXEJ6IFAB5LFWIW")

    response_dict = response.json()

for data in response_dict['dataset']:
    new_pokemon, created = Pokemon.objects.get_or_create(name=data['national_id'])

    new_pokemon.national_id = data['national_id']
    new_pokemon.name = data['name']
    new_pokemon.species = data['species']
    new_genre.save()


    # print data['genre_title']
    # print data['genre_handle']
    # print data['genre_id']
    # print data['genre_parent_id']