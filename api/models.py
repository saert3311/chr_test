from django.db import models

# Create your models here.

class Stations(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7,  null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7,  null=True)
    name = models.CharField(max_length=100,)
    timestamp = models.DateTimeField()
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    address = models.CharField(max_length=100)
    altitude = models.IntegerField()
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