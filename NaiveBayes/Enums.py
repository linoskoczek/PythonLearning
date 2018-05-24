from enum import Enum


class Price(Enum):
    VERY_HIGH = "vhigh"
    HIGH = "high"
    MEDIUM = "med"
    LOW = "low"


class BootSize(Enum):
    HIGH = "high"
    MEDIUM = "med"
    BIG = "big"
    SMALL = "small"


class Capacity(Enum):
    MORE = 'more'
    FOUR = '4'
    THREE = '3'
    TWO = '2'
    ONE = '1'


class CarClass(Enum):
    ACCURATE = "acc"
    GOOD = "good"
    INACCURATE = "unacc"
    VERY_GOOD = "vgood"


class Doors(Enum):
    FOUR = "4"
    MORE_THAN_FIVE = "5more"
    TWO = "2"
    THREE = "3"
    ONE = "1"


class Safety(Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "med"
