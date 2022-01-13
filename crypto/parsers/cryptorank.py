from bs4 import BeautifulSoup
import datetime
from .parser import get_data_from_url

url = 'https://cryptorank.io/ru'

def find_target_data():
    soup = BeautifulSoup(get_data_from_url(url), "lxml")
    table = soup.find("table", class_='table').find("tbody").find_all("tr")[:3]
    data = []
    for trow in table:
        all_spans = trow.find_all('td')[1].find_next().find_all("span")
        title = all_spans[0].text
        price = all_spans[1].text
        data.append({ "title": title, "value": price, "timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") })
    return data