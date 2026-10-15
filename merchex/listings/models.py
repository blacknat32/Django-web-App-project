from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2026)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.name
    
class Band_create(models.Model):
    name = models.fields.CharField(max_length=100)

class Listing(models.Model):
    class Type(models.TextChoices):
        Records = 'disques'
        Clothing = 'vêtements'
        Posters = 'affiches'
        Miscellaneous = 'divers'
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(blank=True, null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

class Listing_create(models.Model):
    name = models.fields.CharField(max_length=100)

class Help(models.Model):
    name = models.fields.CharField(max_length=100)

class Info(models.Model):
    name = models.fields.CharField(max_length=100) 

class Contact(models.Model):
    name = models.fields.CharField(max_length=100)


    
