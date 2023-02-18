from bs4 import BeautifulSoup
import requests
from .models import Proyecto
from datetime import datetime

def get_pages(url:str) -> int:
    """
    Function to get the number of pages
    :param url: to search
    :return: an integer with number of pages
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    select_tag = soup.find('select')
    options_count = len(select_tag.find_all('option'))
    return options_count

def scrap_pages(url:str, pages: int) -> list:
    """
    Function to scrap data from a webpage with table
    :param url:
    :return: A list of objects
    """
    url_generator = (url + str(i) for i in range(pages))

    rows = []

    for page in url_generator:
        response = requests.get(page)
        soup = BeautifulSoup(response.text)

        for row in soup.find_all('tr'):
            columns = row.find_all('td')
            new_item = Proyecto(
                id=columns[0].text.strip(),
                name=columns[1].text.strip(),
                type=columns[2].text.strip(),
                region=columns[3].text.strip(),
                typology=columns[4].text.strip(),
                responsible=columns[5].text.strip(),
                investment=columns[6].text.strip(),
                date=datetime.strptime(columns[6].text.strip(), '%d/%m/%y').date(),
                status=columns[7].text.strip()
            )
            rows.append(new_item)

    return rows