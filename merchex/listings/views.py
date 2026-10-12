# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing, Help, Info


# listings/views.py

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def about(request):
    info = Info.objects.all()
    return render(request, 'listings/about.html', 
            {'info': info})

def listings_list(request):
    listing = Listing.objects.all()
    return render(request, 
            'listings/listings_list.html',
            { 'listings': listing }) 

def listings_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
            'listings/listings_detail.html',
            {'listing': listing})
                

def contact(request):
    help = Help.objects.all()
    return render(request, 'listings/contact.html', 
            {'help': help})