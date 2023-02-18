from django.shortcuts import render
from .stations import import_data
from .models import Stations
from django.http import Http404

# Create your views here.

def bikesantiago_view(request):
    try:
        Stations.objects.all().delete()# lo borramos solo para integrarlos de nuevo en cada request
        station_list = import_data('http://api.citybik.es/v2/networks/bikesantiago')
        station_objects = Stations.objects.bulk_create(station_list)
    except:
        raise Http404('There was an error')
    return render(request, 'bikesantiago.html', {'stations': station_objects})