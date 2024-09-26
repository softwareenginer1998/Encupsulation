import random
import string


class KodGenerator:
    def __init__(self):
        self.__kod = None
    def kod_yaratish(self, uzunlik):

        if uzunlik <= 0:
            raise ValueError


        harflar = string.ascii_letters + string.digits
        self.__kod = ''.join(random.choice(harflar) for _ in range(uzunlik))

    def kod_olish(self, uzunlik):

        if self.__kod is None or len(self.__kod) != uzunlik:
            return "Access Denied"
        return self.__kod



generator = KodGenerator()
generator.kod_yaratish(8)
print(generator.kod_olish(8))
print(generator.kod_olish(6)) 
