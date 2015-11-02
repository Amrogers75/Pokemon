#!/usr/bin/env python
import requests
import os, sys
from StringIO import StringIO
import json
import django
import requests
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Pokemon, Type, Pokedex, Move, Ability, Description, Sprite


counter = 0
while True:
    counter += 1
    string_counter = str(counter)
    response = requests.get('http://pokeapi.co/api/v1/move/'+string_counter)
    data = response.json()
    print data
    print "============="
    print counter

    new_move, created = Move.objects.get_or_create(name=data['name'])

    new_move.type_id = data['id']
    new_move.description = data['description']
    new_move.power = data['power']
    new_move.accuracy = data['accuracy']
    new_move.category = data['category']
    new_move.pp_points = data['pp']

    try:
        new_move.pokemon = Pokemon.objects.get(move=data['objects'][0]['name'][counter].title())

    except:
        print "could not find move"
        new_move.save()   

# Fields:
# name - the resource name e.g. Water.
# type_id - the id of the resource.
# description - a description of the move.
# power - the power of the move.
# accuracy - the accuracy of the move.
# category - the category of the move.
# pp - the pp points of the move.