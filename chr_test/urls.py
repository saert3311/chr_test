"""chr_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from api.views import bikesantiago_view, scrapper_process, list_proyectos, scrapper_render
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bikesantiago/', bikesantiago_view, name='bikesantiago'),
    path('scrapper/', scrapper_render, name='show_page'),
    path('scrapper/refresh/', scrapper_process, name='refresh'),
    path('scrapper/proyectos/', list_proyectos, name='proyectos_json')
]
