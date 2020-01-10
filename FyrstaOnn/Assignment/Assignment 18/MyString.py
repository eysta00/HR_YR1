#class MyString goes here
class MyString:
    def __init__(self, string):
        self.string = string
    
    def __gt__(self,other):
        counter1 = len(self.string)
        counter2 = len(other.string)
        
        if counter1 > counter2:
            return True
        else:
            return False

    def __sub__(self, other):
        counter1 = len(self.string)
        counter2 = len(other.string)
        diff = counter1 - counter2
        return abs(diff)

obj1 = MyString('this is a string')
obj2 = MyString('this is another one')
print(obj1 > obj2)
print(obj1-obj2)