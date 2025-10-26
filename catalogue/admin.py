from django.contrib import admin
from catalogue.models import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    search_fields = ('firstname', 'lastname') 
