# catalogue/views/artist.py

# 🌟 Imports nécessaires
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from catalogue.models import Artist
from catalogue.forms import ArtistForm


# 🧩 1. Afficher la liste de tous les artistes
def index(request):
    artists = Artist.objects.all()
    return render(request, 'artist/index.html', {
        'artists': artists,
    })


# 🧩 2. Afficher la fiche détaillée d’un artiste
def show(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')
    return render(request, 'artist/show.html', {
        'artist': artist,
    })


# 🧩 3. Modifier un artiste existant
def edit(request, artist_id):
    # 1️⃣ On récupère l'artiste à modifier (ou erreur 404 s’il n’existe pas)
    artist = get_object_or_404(Artist, id=artist_id)

    # 2️⃣ On crée le formulaire avec les données existantes
    form = ArtistForm(request.POST or None, instance=artist)

    # 3️⃣ Si le formulaire est envoyé (POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Django met à jour la base
            return redirect('catalogue:artist-index')

    # 4️⃣ Sinon, on affiche la page avec le formulaire prérempli
    return render(request, 'artist/edit.html', {
        'form': form,
        'artist': artist,
    })

# ➕ Créer un nouvel artiste
def create(request):
    # 1️⃣ On prépare un formulaire vide (ou avec données POST si c’est un envoi)
    form = ArtistForm(request.POST or None)

    # 2️⃣ Si le formulaire est envoyé (POST)
    if request.method == 'POST':
        if form.is_valid():        # Django vérifie les champs
            form.save()            # Et enregistre un nouvel artiste dans la base
            return redirect('catalogue:artist-index')

    # 3️⃣ Si on arrive sur la page pour la première fois (GET)
    # on affiche simplement le formulaire vide
    return render(request, 'artist/create.html', {
        'form': form
    })
# ❌ Supprimer un artiste
from django.shortcuts import redirect, render, get_object_or_404

def delete(request, artist_id):
    # 1️⃣ On récupère l’artiste à supprimer
    artist = get_object_or_404(Artist, id=artist_id)

    # 2️⃣ Si on reçoit une requête POST => l’utilisateur a confirmé la suppression
    if request.method == 'POST':
        artist.delete()  # Supprime la ligne dans la base
        return redirect('catalogue:artist-index')  # Retour à la liste

    # 3️⃣ Si ce n’est pas un POST (par ex. GET), on ré-affiche la fiche de l’artiste
    return render(request, 'artist/show.html', {
        'artist': artist
    })
