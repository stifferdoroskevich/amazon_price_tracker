import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/dp/B06XPJML5D/?coliid=IWI4KMIW96G43&colid=3R9LWA1W4T10G&psc=0&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup_clean = BeautifulSoup(page.content, 'html.parser')
    soup=BeautifulSoup(soup_clean.prettify(), 'html.parser')

    title = soup.find(id="ebooksProductTitle").get_text()
    price = soup.find(class_="a-size-base a-color-price a-color-price").get_text().strip()
    converted_price = float(price[1:])

    print(title.strip())
    print(converted_price)
