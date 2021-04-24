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
    path('contact', benog.views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('events/', benog.views.construction, name='events'),
    path('wiki/', benog.views.construction, name='wiki'),
    path('ml/', benog.views.construction, name='ml'),
    path('login/', benog.views.construction, name='login'),
]

handler400 = benog.views.error_view(400, "Request not possible")
handler403 = benog.views.error_view(403, "Not permitted")
handler404 = benog.views.error_view(404, "Not found")
handler500 = benog.views.error_view(500, "Error")
