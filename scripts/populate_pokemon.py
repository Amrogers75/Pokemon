#!/usr/bin/env python
import requests
import os, sys
# from unidecode import unidecode
# from PIL import Image
import requests
import json
import django

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import Pokemon, Type, Pokedex, Description, Sprite, Move
from StringIO import StringIO
from django.template.defaultfilters import slugify

counter = 1
while True:
    string_counter = str(counter)
    response = requests.get('http://pokeapi.co/api/v1/pokemon/'+string_counter) 
    if response.status == 404:
        break
    data = response.json()
    print data['name']
    counter += 1 
    print "============="
    print counter

    new_pokemon, created = Pokemon.objects.get_or_create(name=data['name'])

    # return requests.get(url).json()

    new_pokemon.national_id = data['national_id']
    # new_pokemon.resource_uri = ['resource_uri'] no model made
    # new_pokemon.created = data['created'], time crated in database
    # new_pokemon.modified = data['modified'] tmie modified in database

    abilities_string = ''
    for ability in data['abilities']:
        abilities_string += (ability['name'] + ', ')
    new_pokemon.abilities = abilities_string
    # new_pokemon.abilities = data['abilities']

    # evolutions_string = ''
    # for evelution in data['evolutions']:
    #     evolutions_string += (evelution['detail'] + ', ')
    # new_pokemon.evolutions = evolutions_string
    # new_pokemon.evolutions = data['evolutions']['detail']

    new_pokemon.descriptions = data['descriptions'][1]
    # print "here"

    moves_string = ''
    for move in data['moves']:
        moves_string += (move['name'] + ', ')
        print moves_string
    new_pokemon.moves = moves_string
    # new_pokemon.moves = data['moves']
    # new_pokemon.moves = data['moves'][1]
    # for xcounter in data['moves']:
    # new_pokemon.moves = Move.objects.get(name=data['moves'][xcounter]['name'])
    # new_pokemon.types = Type.objects.get(name=data['type'])
    new_pokemon.types = data['types'][0]
    new_pokemon.catch_rate = data['catch_rate']
    new_pokemon.species = data['species']
    new_pokemon.hp = data['hp']
    new_pokemon.attack = data['attack']
    new_pokemon.defense = data['defense']
    new_pokemon.sp_atk = data['sp_atk']
    new_pokemon.sp_def = data['sp_def']
    new_pokemon.speed = data['speed']
    new_pokemon.total = data['total']
    # new_pokemon.ev_yield = data['ev_yield'] no model made
    new_pokemon.exp = data['exp']
    new_pokemon.growth_rate = data['growth_rate']
    new_pokemon.weight = data['weight']
    new_pokemon.height = data['height']
    new_pokemon.happiness = data['happiness']
    new_pokemon.slug = slugify(data['name'])
    new_pokemon.save()

# for pokemon in Pokemon.objects.all():

#     param_dict = {'api_key': settings.FMAKEY, 'limit': 200, 'national_id': pokemon.national_id}

#     response = requests.get('http://pokeapi.co/api/v1/pokedex/1/', params=param_dict)
#     response = requests.get("https://freemusicarchive.org/api/get/genres.json?api_key=LFXEJ6IFAB5LFWIW")
#     print response
#     response_dict = response.json()


