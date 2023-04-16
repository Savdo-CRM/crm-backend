from enum import Enum


class PageTypes(Enum):
    """ 3 """
    admin = 'admin'
    director = 'director'
    shop = 'shop'
    wearhouse = 'wearhouse'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]