class Rectangle:
    def __init__(self, length=0, width=0):
        
        self.length = int(length)
        self.width = int(width)
        
        if length < 0:
            self.length = 0
        
        if width < 0:
            self.width = 0

    def __repr__(self):
        return "Rectangle({},{})".format(self.length, self.width)
    def __str__(self):
        return "Length: {}, Width: {}".format(self.length, self.width)
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2(self.length + self.width)
    
    def __eq__(self, other):
        area_1 = self.length * self.width
        area_2 = other.length * other.width

        if area_1 == area_2:
            return True
        else:
            return False
    