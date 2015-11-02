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
    response = requests.get('http://pokeapi.co/api/v1/pokedex/')
    if response.status == 404:
        break
    data = response.json()
    print data['objects'][0]['pokemon'][counter]['name']
    print "============="
    print counter

    new_pokedex, created = Pokedex.objects.get_or_create(name=data['objects'][0]['pokemon'][counter]['name'])
    print data['objects'][0]['pokemon'][counter]['name'].title()

    new_pokedex.name = data['objects'][0]['pokemon'][counter]['name']
    try:
        new_pokedex.pokemon = Pokemon.objects.get(name=data['objects'][0]['pokemon'][counter]['name'].title())
    
        new_pokedex.save()
    except:
        print "could not find pokemon"


# Fields:

# name - the pokedex name e.g. National.
# pokemon - a big list of pokemon within this pokedex.
