from django.db import models

# listings/models.py

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

class Listing(models.Model):
    name = models.fields.CharField(max_length=100)

class Help(models.Model):
    name = models.fields.CharField(max_length=100)

class Info(models.Model):
    name = models.fields.CharField(max_length=100)