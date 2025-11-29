# catalogue/urls.py
from django.urls import path
from . import views  # ✅ on importe views complet 

app_name = 'catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist-index'),
    path('artist/<int:artist_id>/', views.artist.show, name='artist-show'),
    path('artist/create', views.artist.create, name='artist-create'),
    path('artist/edit/<int:artist_id>', views.artist.edit, name='artist-edit'),
    path('artist/delete/<int:artist_id>', views.artist.delete, name='artist-delete'),
    path('type/', views.type.index, name='type-index'),
    path('type/<int:type_id>', views.type.show, name='type-show'),

]


