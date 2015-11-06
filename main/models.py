from django.db import models
from django.utils.http import urlquote
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from vote.managers import VotableManager
from dynamic_scraper.models import Scraper
# from scrapy.contrib.url import CardView

# Create your models here.

# add a votting/trending model


class Pokemon(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    national_id = models.IntegerField(null=True, blank=True)
    evolutions = models.CharField(max_length=255, null=True, blank=True)
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
    type = models.ForeignKey('main.Type', null=True)
    votes = VotableManager()
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    ineffective = models.TextField(null=True, blank=True)
    no_effect = models.CharField(max_length=255, null=True, blank=True)
    resistance = models.CharField(max_length=255, null=True, blank=True)
    super_effective = models.TextField(null=True, blank=True)
    weakness = models.TextField(null=True, blank=True)
    

    def __unicode__(self):
        return unicode(self.name)


class Ability(models.Model):
    description = models.TextField(null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    pokemon = models.ManyToManyField('main.Pokemon', null=True)

    def __unicode__(self):
        return unicode(self.name)


class Description(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    games = models.CharField(max_length=255, null=True, blank=True)
    pokemon = models.ForeignKey('main.Pokemon', null=True)
    image = models.ImageField(upload_to=pokemon)

    def __unicode__(self):
        return self.name


class Move(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    power = models.IntegerField(null=True, blank=True)
    accuracy = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    pp_points = models.IntegerField(null=True, blank=True)
    pokemon = models.ManyToManyField('main.Pokemon', null=True)

    def __unicode__(self):
        return '%s' % self.name


class Pokedex(models.Model):  
    name = models.CharField(max_length=255, null=True, blank=True)
    pokemon = models.ForeignKey('main.Pokemon', null=True)

    def __unicode__(self):
        return self.name


class Sprite(models.Model):
    pokemon = models.ForeignKey('main.Pokemon', null=True) 
    name = models.CharField(max_length=255, null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=pokemon)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class CardView(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
#     scraper = models.ForeignKey(Scraper, blank=True, null=True)

    def __unicode__(self):
        return self.name


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if username != None:
            email = username

        if not email:
            raise ValueError("Email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email,
                        is_staff=is_staff,
                        is_active=True,
                        is_superuser=is_superuser,
                        last_login=now,
                        date_joined=now,
                        **extra_fields
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email=None, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
