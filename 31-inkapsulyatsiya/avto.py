
from uuid import uuid4
class Avto:
    __num_avto = 0
    PI = 3.14159
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    
# Klassgaoid metodlar

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
class Bus:
    pass

class Train:
    pass
