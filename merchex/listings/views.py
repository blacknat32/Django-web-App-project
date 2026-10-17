# ~/projects/django-web-app/merchex/listings/views.py

from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Contact, Listing, Help, Info, Band_create
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.shortcuts import redirect  # ajoutez cet import
from django.core.mail import send_mail

# listings/views.py

def contact(request):

 # ...nous pouvons supprimer les déclarations de journalisation qui étaient ici...

        if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
                form = ContactUsForm(request.POST)
                if form.is_valid():
                        send_mail(
                        subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                        message=form.cleaned_data['message'],
                        from_email=form.cleaned_data['email'],
                        recipient_list=['admin@merchex.xyz'],
                        )
                return redirect('email-sent')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
        else:
 # ceci doit être une requête GET, donc créer un formulaire vide
                form = ContactUsForm()

        return render(request,
                'listings/contact.html',
                {'form': form})

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_change(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)

        if form.is_valid():
                form.save()
                return redirect('band-detail', band.id)

    else:
        form = BandForm(instance=band)

    return render(request,
            'listings/band_change.html',
            {'form': form })

def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def about(request):
    info = Info.objects.all()
    return render(request, 'listings/about.html', 
            {'info': info})

def email_sent(request):
        contact = Contact.objects.all()
        return render(request, 'listings/email_sent.html',
                {'contact' : contact}) 

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

def listings_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Listing » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listings-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listings_create.html',
            {'form': form})

def listings_change(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)

        if form.is_valid():
                form.save()
                return redirect('listings-detail', listing.id)

    else:
        form = ListingForm(instance=listing)

    return render(request,
            'listings/listings_change.html',
            {'form': form })

def listings_delete(request, id):
    listing = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer l'annonce de la base de données
        listing.delete()
        # rediriger vers la liste des annonces
        return redirect('listings-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/listings_delete.html',
                    {'listing': listing})




