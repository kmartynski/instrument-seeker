from typing import Any, Dict

from email_dispatcher import send_email
from piano_seeker import PianoFinder


pianos = ["YAMAHA CP-60M", "YAMAHA CP-70B", "YAMAHA CP-80B", "FENDER RHODES MK 1", "FENDER RHODES MK 2"]

results: Dict[str, Any] = {}


def main():
    for piano in pianos:
        finder = PianoFinder(piano)
        results[piano] = finder.get_offers()

    send_email(results)


if __name__ == "__main__":
    main()
