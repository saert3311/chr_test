from django.shortcuts import render
from .stations import import_data
from .models import *
from .scrapper import scrap_pages, get_pages
from .snifa_scrapper import snifa_scrap
from django.http import Http404, JsonResponse
from rest_framework import mixins, generics
from .serializers import ProyectoSerializer, ProcedimientosSerializer
from rest_framework.response import Response

# Create your views here.
def index_view(request):
    return render(request, 'index.html')
def citibik_view(request, city):
    try:
        Stations.objects.all().delete()# lo borramos solo para integrarlos de nuevo en cada request
        station_list = import_data(f'http://api.citybik.es/v2/networks/{city}')
        station_objects = Stations.objects.bulk_create(station_list)
    except Exception as e:
        print(e)
        raise Http404('There was an error')
    return render(request, 'citybik.html', {'stations': station_objects, 'city': city})

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

def snifa_scrapper_render(request):
    return render(request, 'snifa_scrapper.html')

def snifa_scrapper_process(request):
    Procedimientos.objects.all().delete()
    lista_procedimientos = snifa_scrap('https://snifa.sma.gob.cl/Sancionatorio/Resultado')
    procedimientos_objects = Procedimientos.objects.bulk_create(lista_procedimientos)
    return JsonResponse({'result':'ok'})

class listProcedimmientosView(mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Procedimientos.objects.all()
    serializer_class = ProcedimientosSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

snifa_list_procedimientos = listProcedimmientosView.as_view()
