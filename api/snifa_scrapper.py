from bs4 import BeautifulSoup
import requests
from .models import Procedimientos
from datetime import datetime
def snifa_scrap(url:str) -> list:
    """
    Funcion para scrappear una pagina individual
    :param url: url para scrappear
    :return: list de objetos de Procedientos
    """
    row_data = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cols = len(soup.find_all('th'))

    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 0 or len(columns) != cols:  # con esto omitimos la primera fila de los headers
            continue
        new_item = Procedimientos(
            id=int(columns[0].text.strip()),
            expediente=columns[1].text.strip(),
            unidad=columns[2].text.strip(),
            nombre=columns[3].text.strip(),
            categoria=columns[4].text.strip(),
            region=columns[5].text.strip(),
            estado=columns[6].text.strip(),
            detalle=columns[7].a['href']
        )
        row_data.append(new_item)
    return row_data