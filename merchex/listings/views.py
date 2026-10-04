# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
            <li>{bands[3].name}</li>
        </ul>
""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    listing = Listing.objects.all()
    return HttpResponse(f"""
            <h1>Hello Django !</h1>
            <p>le truc qu'on m'a dit d'écrire :<p>
            <ul>
                <li>{listing[0].name}</li>
                <li>{listing[1].name}</li>
                <li>{listing[2].name}</li>
                <li>{listing[3].name}</li>
            </ul>
""")

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Nous contacter :</p>')