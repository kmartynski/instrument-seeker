from bs4 import BeautifulSoup, ResultSet, PageElement
import requests
from typing import Dict, List, Union

from enums import PianoCondition


PIANO_PAGES_MAPPING: Dict[str, str] = {
    "YAMAHA CP-60M": "https://www.ebay.com/sch/i.html?_nkw=yamaha+cp+60+m",
    "YAMAHA CP-70B": "https://www.ebay.com/sch/i.html?_nkw=yamaha+cp+70+b",
    "YAMAHA CP-80B": "https://www.ebay.com/sch/i.html?_nkw=yamaha+cp+80+b",
    "FENDER RHODES MK 1": "https://www.ebay.com/sch/i.html?_nkw=fender+rhodes+mk+1",
    "FENDER RHODES MK 2": "https://www.ebay.com/sch/i.html?_nkw=fender+rhodes+mk+2",
}


class PianoFinder:

    def __init__(self, piano_name: str):
        self.piano_name = piano_name

    def get_offers(self) -> Union[Dict[str, List[str]], None]:
        list_of_elements = self._get_list_of_pianos()
        accepted_conditions = [
            PianoCondition.PRE_OWNED.value,
            PianoCondition.REFURBISHED.value,
            PianoCondition.OPEN_BOX.value
        ]
        validated_offers = {}
        for count, element in enumerate(list_of_elements):
            if count > 5:
                break
            if self._get_piano_condition(element) not in accepted_conditions:
                continue
            condition = self._get_piano_condition(element)
            price = self._get_price(element)
            url = self._get_url_to_product(element)

            new_record = {f"{self.piano_name} - {count}": [condition, price, url]}
            validated_offers.update(new_record)
        return validated_offers

    def _get_ebay_auction_for_concrete_piano(self) -> requests.Response:
        auction = requests.get(PIANO_PAGES_MAPPING[self.piano_name])
        return auction

    def _get_auction_content(self) -> BeautifulSoup:
        content = BeautifulSoup(self._get_ebay_auction_for_concrete_piano().content, "html.parser")
        return content

    def _get_list_of_pianos(self) -> ResultSet:
        result = self._get_auction_content().find("div", {"class": "srp-river-results"}).find("ul", recursive=False).\
            find_all("li", recursive=False)
        return result

    def _get_price(self, element: PageElement) -> str:
        return element.find_next("span", {"class": "ITALIC"}).text

    def _get_url_to_product(self, element: PageElement) -> str:
        a_tag = element.find_next("a", href=True)
        return a_tag["href"]

    def _get_piano_condition(self, element: PageElement) -> str:
        return element.find_next("span", {"class": "SECONDARY_INFO"}).text
