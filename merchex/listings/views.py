# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing, Help, Info


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', 
            {'bands': bands})

def about(request):
    info = Info.objects.all()
    return render(request, 'listings/about.html', 
            {'info': info})

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
    help = Help.objects.all()
    return render(request, 'listings/contact.html', 
            {'help': help})