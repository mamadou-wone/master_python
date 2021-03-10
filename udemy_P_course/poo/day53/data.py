from bs4 import BeautifulSoup
import requests
from pprint import pprint
endpoint = "https://www.expat-dakar.com"
class Data:
    def __init__(self, url):
        self.url = url
        header = {
            "Accept-Language": "en-GB,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        self.response = requests.get(url, headers=header)
        data = self.response.text
        self.soup = BeautifulSoup(data, "html.parser")
        # pprint(self.soup)


    def list_of_links(self):
        all_link = self.soup.select(selector="h2 a")
        url = []
        for link in all_link:
            url.append(endpoint+link.get("href"))
        return url

    def get_price(self):
        all_price = self.soup.select(selector=".ad-item-price span")
        prices = []
        for price in all_price:
            prices.append(price.getText().strip())
        return prices


    def get_address(self):
        all_address = self.soup.select(selector="h2 a")
        address = []
        for item in all_address:
            address.append(item.getText().strip())
        return address
