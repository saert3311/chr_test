from django.shortcuts import render
from .stations import import_data
from .models import Stations, Proyecto
from .scrapper import scrap_pages, get_pages
from django.http import Http404, JsonResponse
from rest_framework import mixins, generics
from .serializers import ProyectoSerializer
from rest_framework.response import Response

# Create your views here.

def bikesantiago_view(request):
    try:
        Stations.objects.all().delete()# lo borramos solo para integrarlos de nuevo en cada request
        station_list = import_data('http://api.citybik.es/v2/networks/bikesantiago')
        station_objects = Stations.objects.bulk_create(station_list)
    except:
        raise Http404('There was an error')
    return render(request, 'bikesantiago.html', {'stations': station_objects})

def scrapper_process(request):
    Proyecto.objects.all().delete()
    pages = get_pages('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php')
    project_list = scrap_pages('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual=', pages)
    project_objects = Proyecto.objects.bulk_create(project_list)
    return JsonResponse({'result':'ok'})


class listProjectsView(mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

list_proyectos = listProjectsView.as_view()

def scrapper_render(request):
    return render(request, 'seia.html')