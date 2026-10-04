# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django !</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Voici nos produits disponibles.</p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Nous contacter :</p>')