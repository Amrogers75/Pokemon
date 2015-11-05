#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
from PIL import Image
import requests
import json
import django

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import Pokemon, Type, Pokedex, Description, Sprite, Move, Ability
from StringIO import StringIO
from django.template.defaultfilters import slugify

counter = 1
while True:
    string_counter = str(counter)
    response = requests.get('http://pokeapi.co/api/v1/pokemon/'+string_counter) 
    # if response.status == 404:
    #     break
    data = response.json()
    print data['name']
    counter += 1 
    print "============="
    print counter

    new_pokemon, created = Pokemon.objects.get_or_create(name=data['name'])

    # return requests.get(url).json()

    new_pokemon.national_id = data['national_id']

    abilities_string = ''
    print data['abilities']
    for ability in data['abilities']:
        abilities_string = (ability['name'] + ', ')
        ability_obj, created = Ability.objects.get_or_create(name=ability['name'])
        print ability_obj
        ability_obj.pokemon = new_pokemon
        print new_pokemon
        ability_obj.save()
    # new_pokemon.abilities = data['abilities']

    evolutions_string = ''
    for evelution in data['evolutions']:
        evolutions_string = (evelution['method'] + ', ')
        evolution.save()
    # new_pokemon.evolutions = evolutions_string
    # new_pokemon.evolutions = data['evolutions']['detail']

    new_pokemon.description = Description.objects.filter(name=data['descriptions'][0]['name'])

# Model.objects.filter(field_name=some_param)

    moves_string = ''
    for move in data['moves']:
        moves_string += (move['name'] + ', ')
        move_obj, created = Move.objects.get_or_create(name__iexact=move['name'])
        move_obj.Pokemon = new_pokemon
        move_obj.save()

    new_pokemon.sprite = Sprite.objects.filter(name=data['sprites'][0]['name'])

    new_pokemon, created = Type.objects.get_or_create(name__icontains=data['types'][0]['name'])
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




