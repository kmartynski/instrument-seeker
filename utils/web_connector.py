from bs4 import BeautifulSoup
import requests


class WebConnector:

    def __init__(self, url: str):
        self.url = url

    def get_content(self, id_name):
        website = self._get_landing_page()
        soup = BeautifulSoup(website.content, 'html5lib')
        search_bar = soup.find('div', attrs={'id': id_name})
        return search_bar

    def _get_landing_page(self) -> requests.Response:
        req = requests.get(self.url)
        return req
