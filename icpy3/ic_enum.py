__author__ = 'amryf'

from enum import Enum

class COLORFORMAT(Enum):
    Y800 = 0
    RGB24 = 1
    RGB32 = 2
    UYVY = 3
    Y16 = 4
    NONE = 5

class IMG_FILETYPE(Enum):
    FILETYPE_BMP = 0
    FILETYPE_JPEG = 0
