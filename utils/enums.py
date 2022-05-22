from enum import Enum


class Piano(str, Enum):
    RHODES_MK1 = "Fender Rhodes MK1"
    RHODES_MK2 = "Fender Rhodes MK2"
    YAMAHA_CP_60 = "Yamaha CP60M"
    YAMAHA_CP_70 = "Yamaha CP70B"
    YAMAHA_CP_80 = "Yamaha CP80B"


class Site(str, Enum):
    EBAY = "www.ebay.pl"
    OLX = "www.olx.pl"
