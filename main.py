from piano_seeker import PianoFinder


pianos = ["YAMAHA CP-60M", "YAMAHA CP-70B", "YAMAHA CP-80B", "FENDER RHODES MK 1", "FENDER RHODES MK 2"]


def main():
    for piano in pianos:
        finder = PianoFinder(piano)
        finder.get_offers()


if __name__ == "__main__":
    main()
