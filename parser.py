# create parser beautiful soup 4 and requests
import requests
from bs4 import BeautifulSoup

def get_currency(code):

    # parsing google.com
    url = "https://www.banki.ru/products/currency/cb"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    # continue

    # find <tr> element with data-currency-code attribute
    currency = soup.find("tr", attrs={"data-currency-code": code}).find_all("td")[-2].string.strip()
    count = soup.find("tr", attrs={"data-currency-code": code}).find_all("td")[1].string.strip()
    return float(currency) / float(count)