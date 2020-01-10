#class Pair goes here
class Pair:
    def __init__(self, v1=0, v2=0):
        self.v1 = int(v1)
        self.v2 = int(v2)
    
    def __str__(self):
        return 'Value 1: {}, Value 2: {}'.format(self.v1, self.v2)
    
    def __add__(self, other):
        sum1 = self.v1 + other.v1
        sum2 = self.v2 + other.v2
        return Pair(sum1, sum2)