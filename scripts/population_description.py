#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
from PIL import Image
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

from main.models import Pokemon, Type, Ability, Pokedex, Move, Description, Sprite


counter = 1
while True:
    counter += 1
    string_counter = str(counter)
    response = requests.get('http://pokeapi.co/api/v1/description/'+string_counter)  
    data = response.json()
    if response.status == 404:
        break
    print data['name']
    print "============="
    print counter

    new_description, created = Description.objects.get_or_create(name=data['name'])

    new_description.type_id = data['id']
    # print data['pokemon']['name']
    try:
        new_description.pokemon = Pokemon.objects.get(name=data['pokemon']['name'].title())
    
    except:
        print "could not find pokemon"
    new_description.games = data['games']
    new_description.save()

# Fields:
# name - the resource name.
# id - the id of the resource.
# resource_uri - the uri of this resource.
# created - the creation date of the resource.
# modified - the last time this resource was modified.
# games - a list of games this description is in.
# pokemon - the pokemon this sprite is for.