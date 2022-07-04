from typing import Dict

from piano_seeker import PianoFinder


PIANO_PAGES_MAPPING: Dict[str, str] = {
    "YAMAHA CP-60M": "https://www.ebay.com/sch/i.html?_nkw=yamaha+cp+60+m",
    "YAMAHA CP-70B": "https://www.ebay.com/sch/i.html?_nkw=yamaha+cp+70+b",
    "YAMAHA CP-80B": "https://www.ebay.com/sch/i.html?_nkw=yamaha+cp+80+b",
    "FENDER RHODES MK 1": "https://www.ebay.com/sch/i.html?_nkw=fender+rhodes+mk+1",
    "FENDER RHODES MK 2": "https://www.ebay.com/sch/i.html?_nkw=fender+rhodes+mk+2",
}


def main():
    for piano in PIANO_PAGES_MAPPING.keys():
        finder = PianoFinder(piano)
        finder.get_offers()

