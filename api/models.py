from django.db import models

# Create your models here.

class Stations(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7,  null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7,  null=True)
    name = models.CharField(max_length=200,)
    timestamp = models.DateTimeField()
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    address = models.CharField(max_length=200)
    altitude = models.IntegerField(null=True, blank=True)
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.DateTimeField()
    normal_bikes = models.IntegerField()
    payment = models.JSONField()
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=20, blank=True, null=True) #la documentacion de la api no dice cuales son campos opcionales
    renting = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


    class Meta:
        ordering = ['-id']

class Proyecto(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    type = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    typology = models.CharField(max_length=10)
    responsible = models.CharField(max_length=250)
    investment = models.CharField(max_length=50) #podria ser en otro formato para comparar
    date = models.DateField()
    status = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} - {self.responsible}'

    class Meta:
        ordering = ['-id']

class Procedimientos(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Nro')
    expediente = models.CharField(max_length=25, verbose_name='Expediente')
    unidad = models.CharField(max_length=400, verbose_name='Unidad Fiscalizable')
    nombre = models.CharField(max_length=400, verbose_name='Nombre o razón social')
    categoria = models.CharField(max_length=200, verbose_name='Categoría')
    region = models.CharField(max_length=100, verbose_name='Región') # esto se podria mejorar con normalizacion
    estado = models.CharField(max_length=50, verbose_name='Estado') # y esto tambien
    detalle = models.URLField(verbose_name='Enlace detalle')

    def __str__(self):
        return f'{self.id} - {self.nombre}'

    class Meta:
        ordering = ['-id']