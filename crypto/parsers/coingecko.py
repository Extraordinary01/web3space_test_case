from bs4 import BeautifulSoup
import datetime
from .parser import get_data_from_url

url = 'https://www.coingecko.com/en'

def find_target_data():
    soup = BeautifulSoup(get_data_from_url(url), "lxml")
    trows = soup.find("tbody").find_all("tr")[:65]
    data = []
    for item in trows:
        title = item.find("td", class_="coin-name")["data-sort"]
        price = item.find("td", class_="price").find_next().text
        data.append({ "title": title, "value": price, "timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") })
    return data
