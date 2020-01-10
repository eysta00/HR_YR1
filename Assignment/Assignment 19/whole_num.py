class WholeNumber():
    def __init__(self, num = 0):
        if type(num) == int and num >= 0:
            self.__num = num
        else:
            self.__num = None
    
    def __str__(self):
        return str(self.__num)
    
    def __add__(self, other):
        try:
            return WholeNumber(self.__num + other.__num)
        except TypeError:
            return None
    
    def __sub__(self, other):
        try:
            return WholeNumber(self.__num - other.__num)
        except TypeError:
            return None
    
    def __mul__(self, other):
        try:
            return WholeNumber(self.__num * other.__num)
        except TypeError:
            return None