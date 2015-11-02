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
    response = requests.get('http://pokeapi.co/api/v1/sprite/'+string_counter)  
    data = response.json()
    print data['name']
    print "============="
    print counter

    new_sprite, created = Sprite.objects.get_or_create(name=data['name'])
    try:
        new_sprite.pokemon = Pokemon.objects.get(name=data['objects'][0]['name'][counter].title())

    except:
        print "could not find sprite"

    new_sprite.type_id = data['id']
    new_sprite.image = data['image']
    new_sprite.save()

# Fields:
# name - the resource name.
# id - the id of the resource.
# pokemon - the pokemon this sprite is for.
# image - the uri for the sprite image