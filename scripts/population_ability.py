#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
# from PIL import Image
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
    response = requests.get('http://pokeapi.co/api/v1/ability/'+string_counter) 
    # if response.status == 404:
    #     break 
    data = response.json()
    print data['name']
    print "============="
    print counter

    new_ability, created = Ability.objects.get_or_create(name=data['name'])
    print data['description']
    # new_ability.name = data['name']
    new_ability.type_id = data['id']
    new_ability.description = data['description']
    new_ability.save()

# Fields
# name - the resource name e.g. Overgrow.
# id - the id of the resource.
# description - the description of this ability