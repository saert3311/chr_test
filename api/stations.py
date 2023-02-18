import requests
from .models import Stations
from datetime import datetime
from django.utils.timezone import make_aware

def flatten_dict(d) -> dict:
    """
    Function to flatten a dict, without the nested dict key
    :param d: the dict to flatten
    :return: the flattened dict
    """
    items = []
    for k, v in d.items():
        if isinstance(v, dict):
            items.extend(flatten_dict(v).items())
        else:
            items.append((k, v))
    return dict(items)

def format_datetimes_with_tz(input: str) -> datetime:
    """
    Function to transform str to a datetime object an add TZ info
    :param input: and ISO 8601 string datetime
    :return: datetime object with TZ info
    """
    datetime_object = datetime.strptime(input, '%Y-%m-%dT%H:%M:%S.%f%z')
    if datetime_object.tzinfo is None or datetime_object.tzinfo.utcoffset(datetime_object) is None:
        aware_datetime = make_aware(datetime_object)
        return aware_datetime
    return datetime_object

def import_data(endpoint: str) -> list:
    """
    Function to request data to an endpoint and return a dict
    :param endpoint: an str with the address to check
    :return: a list of Stations
    """
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
    flatenned_data = [flatten_dict(item) for item in data['network']['stations']]
    data_objects = [
        Stations( #No use unpacking ** por que la api puede cambiar y quebrar el programa y debugear seria mas dificl
            id=item.get('id'),
            latitude=item.get('latitude'),
            longitude=item.get('longitude'),
            name=item.get('name'),
            timestamp=format_datetimes_with_tz(item.get('timestamp')),
            empty_slots=item.get('empty_slots'),
            free_bikes=item.get('free_bikes'),
            address=item.get('address'),
            altitude=item.get('altitude'),
            ebikes=item.get('ebikes'),
            has_ebikes=item.get('has_ebikes'),
            last_updated=make_aware(datetime.fromtimestamp(item.get('last_updated'))),
            normal_bikes=item.get('normal_bikes'),
            payment=item.get('payment'),
            payment_terminal=item.get('payment-terminal'),
            renting=item.get('renting'),
            slots=item.get('slots'),
            uid=item.get('uid'),
            post_code=item.get('post_code')
        ) for item in flatenned_data
    ]
    return data_objects