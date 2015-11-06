#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
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

Type.objects.filter(name=None).delete()

counter = 1
while True:
    string_counter = str(counter)
    response = requests.get('http://pokeapi.co/api/v1/pokemon/'+string_counter) 

    data = response.json()
    print data['name']
    counter += 1 
    print "============="
    print counter

    print data['types'][0]['name']

    new_pokemon, created = Pokemon.objects.get_or_create(name=data['name'])
    
    new_pokemon.catch_rate = data['catch_rate']
    new_pokemon.species = data['species']
    new_pokemon.hp = data['hp']
    new_pokemon.attack = data['attack']
    new_pokemon.defense = data['defense']
    new_pokemon.sp_atk = data['sp_atk']
    new_pokemon.sp_def = data['sp_def']
    new_pokemon.speed = data['speed']
    new_pokemon.total = data['total']
    new_pokemon.national_id = data['national_id']
    new_pokemon.exp = data['exp']
    new_pokemon.growth_rate = data['growth_rate']
    new_pokemon.weight = data['weight']
    new_pokemon.height = data['height']
    new_pokemon.happiness = data['happiness']
    new_pokemon.slug = slugify(data['name'])
    new_pokemon.save()

    print "Type %s" % data['types'][0]['name']
    if data['types'][0]['name'] != None:
        type_obj, created = Type.objects.get_or_create(name__iexact=data['types'][0]['name'])        
        new_pokemon.type = type_obj
        new_pokemon.save()

    for ability in data['abilities']:
        ability_obj, created = Ability.objects.get_or_create(name=ability['name'])
        ability_obj.pokemon.add(new_pokemon)  

    for move in data['moves']:
        print "### MOVE: %s" % move['name']
        if move['name'] != '' and move['name'] != None:
            move_obj, created = Move.objects.get_or_create(name__iexact=move['name'])
            move_obj.pokemon.add(new_pokemon)

            print "Pokemon Moves %s" % move_obj.pokemon.all()




    # new_pokemon.description = Description.objects.filter(name=data['descriptions'][0]['name'])
    
    # new_pokemon.ev_yield = data['ev_yield'] no model made

    # evolutions_string = ''
    # for evelution in data['evolutions']:
    #     evolutions_string = (evelution['method'] + ', ')
    #     evolution.save()
    # new_pokemon.evolutions = evolutions_string
    # new_pokemon.evolutions = data['evolutions']['detail']

    # new_pokemon.sprite = Sprite.objects.filter(name=data['sprites'][0]['name'])





