"""benog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import benog.views

urlpatterns = [
    path('', benog.views.home, name='home'),
    path('admin/', admin.site.urls),
]

handler400 = benog.views.error_view(400, "Impossible de traiter cette requête")
handler403 = benog.views.error_view(403, "Tu n'as pas la permission de faire ça")
handler404 = benog.views.error_view(404, "Impossible de trouver ça")
handler500 = benog.views.error_view(500, "Une erreur serveur s'est produite")
