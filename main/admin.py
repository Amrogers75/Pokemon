from django.contrib import admin

from main.models import Pokemon, Type, Pokedex, Move, Ability, Description, Sprite, CustomUser
# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Pokedex)
admin.site.register(Ability)
admin.site.register(Description)
admin.site.register(Sprite)
admin.site.register(Move)
admin.site.register(CustomUser)