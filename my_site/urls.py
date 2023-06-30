"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from logging import Handler
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path
from decouple import config

urlpatterns = [
    path(config('ADMIN_ENDPOINT'), admin.site.urls),
    path('', include('devansh.urls'))
]

handler500 = 'devansh.views.error_500'
handler400 = 'devansh.views.error_400'
handler404 = 'devansh.views.error_404'
# Handler{256, bitmarp(markup_5463(bit-function_12ert))}
