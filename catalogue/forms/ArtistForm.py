from django import forms
from catalogue.models import Artist

# 🧩 Ce formulaire est "lié" au modèle Artist.
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist  # On dit à Django quel modèle utiliser
        fields = ['firstname', 'lastname']  # Les champs du formulaire
