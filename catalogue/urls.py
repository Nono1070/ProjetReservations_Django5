# catalogue/urls.py

from django.urls import path
from .views import artist

app_name = 'catalogue'

urlpatterns = [
    path('artist/', artist.index, name='artist-index'),
    path('artist/<int:artist_id>/', artist.show, name='artist-show'),
]


