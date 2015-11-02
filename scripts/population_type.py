#!/usr/bin/env python
import requests
import os, sys
# from unidecode import unidecode
# from PIL import Image
import json
import django
import requests
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from StringIO import StringIO

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from main.models import Pokemon, Type, Pokedex, Ability, Description, Sprite, Move


counter = 1
while True:
    counter += 1
    string_counter = str(counter)
    response = requests.get('http://pokeapi.co/api/v1/type/'+string_counter)  
    data = response.json()
    print data['name']
    print "============="
    print counter

    new_type, created = Type.objects.get_or_create(type_id=data['id'])

    # return requests.get(url).json()

    new_type.name = data['name']
    # new_type.type_id = data['id'][1]
    new_type.ineffective = data['ineffective']
    new_type.no_effect = data['no_effect']
    new_type.resistance = data['resistance']
    new_type.super_effective = data['super_effective']
    new_type.weakness = data['weakness']
    new_type.save()
    

# Field
# name - the resource name e.g. Water.
# id - the id of the resource.
# ineffective - the types this type is ineffective against.
# no_effect - the types this type has no effect against.
# resistance - the types this type is resistant to.
# super_effective - the types this type is super effective against.
# weakness - the types this type is weak to.