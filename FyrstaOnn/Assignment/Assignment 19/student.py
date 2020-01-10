
class Student:
    def __init__(self, id, float_lst):
        self.id = id
        self.float_lst = float_lst
    
    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.id, self.float_lst)

    def __gt__(self, other):
        return self.get_avrg() > other.get_avrg()
        

    def get_avrg(self):
        total = 0
        for grade in self.float_lst:
            total += grade
        return total / len(self.float_lst)