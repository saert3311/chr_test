from http.client import RemoteDisconnected

from bs4 import BeautifulSoup
import requests
from .models import Proyecto
from datetime import datetime
import concurrent.futures

def get_pages(url:str) -> int:
    """
    Function to get the number of pages
    :param url: to search
    :return: an integer with number of pages
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    select_tag = soup.find('select')
    options_count = len(select_tag.find_all('option'))
    return options_count

def scrap_pages(url:str, pages: int) -> list:
    """
    Function to scrap data from a webpage with table
    :param url:
    :return: A list of objects
    """
    url_generator = (url + str(i) for i in range(1, pages))

    rows = []
    try:
        with concurrent.futures.ThreadPoolExecutor(100) as executor:
            futures = [executor.submit(scrap_page, url) for url in url_generator]

        for future in concurrent.futures.as_completed(futures):
            data = future.result()
            rows.extend(data)
        return rows
    except RemoteDisconnected as e:
        print(e)
        return rows
def scrap_page(url:str) -> list:
    """
    Function to scrap an individual page
    :param url: url to scrap
    :return: list of Proyecto objects
    """
    row_data = []
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cols = len(soup.find_all('th'))

    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 0 or len(columns) != cols:  # con esto omitimos la primera fila de los headers
            continue
        new_item = Proyecto(
            id=int(columns[0].text.strip()),
            name=columns[1].text.strip(),
            type=columns[2].text.strip(),
            region=columns[3].text.strip(),
            typology=columns[4].text.strip(),
            responsible=columns[5].text.strip(),
            investment=columns[6].text.strip(),
            date=datetime.strptime(columns[7].text.strip(), '%d/%m/%Y').date(),
            status=columns[8].text.strip()
        )
        row_data.append(new_item)
    return row_data