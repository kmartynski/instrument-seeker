from enum import Enum


class Pianos(str, Enum):
    FENDER_RHODES_MK_1 = "FENDER RHODES MK 1"
    FENDER_RHODES_MK_2 = "FENDER RHODES MK 2"
    YAMAHA_CP_60_M = "YAMAHA CP-60M"
    YAMAHA_CP_70_B = "YAMAHA CP-70B"
    YAMAHA_CP_80_B = "YAMAHA CP-80B"


class PianoCondition(str, Enum):
    BRAND_NEW = "Brand New"
    OPEN_BOX = "Open Box"
    PARTS_ONLY = "Parts Only"
    PRE_OWNED = "Pre-Owned"
    REFURBISHED = "Refurbished"
