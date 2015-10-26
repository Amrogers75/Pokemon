from django.db import models
from django.utils.http import urlquote
# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    national_id = models.IntegerField(null=True, blank=True)
    # resource_uri - the uri of this resource.
    created = models.FloatField(null=True, blank=True)
    modified = models.FloatField(null=True, blank=True)
    abilities = models.CharField(max_length=255, null=True, blank=True)
    evolutions = models.IntegerField(null=True, blank=True)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    moves = models.IntegerField(null=True, blank=True)
    types = models.CharField(max_length=255, null=True, blank=True)
    catch_rate = models.IntegerField(null=True, blank=True)
    species = models.CharField(max_length=255, null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    sp_atk = models.IntegerField(null=True, blank=True)
    sp_def = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    # ev_yield - the ev yield for this pokemon.
    exp = models.IntegerField(null=True, blank=True)
    growth_rate = models.CharField(max_length=255, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    happiness = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.pokemon_name


