from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# ✅ On crée notre propre vue de déconnexion GET
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

urlpatterns = [
    # 🏠 Page d'accueil
    path('', lambda request: redirect('catalogue:artist-index')),

    # 🎨 App Catalogue
    path('catalogue/', include('catalogue.urls')),

    # 🔐 Connexion / Déconnexion
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # ⚙️ Admin
    path('admin/', admin.site.urls),
]

