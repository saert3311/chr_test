from django.test import TestCase
from .stations import import_data
from .models import Stations
# Create your tests here.

class ImportDataTestCase(TestCase):
    def test_import_data(self):
        station_list =import_data('http://api.citybik.es/v2/networks/bikesantiago')
        station_objects = Stations.objects.bulk_create(station_list)
        self.assertEqual(len(station_objects), len(station_list))

