import operator

NUM_OF_GRADES = 3
NUM_OF_STUDENTS = 4

def get_grades ():
    '''Function asks user for a name and grades, it returns a dictionary where
    the key is the name and the grades are a list of float numbers'''
    value_grade_lst = []
    grades_dict = {}

    for _ in range(NUM_OF_STUDENTS):
        key_name = input("Student name: ")

        for i in range(NUM_OF_GRADES):
            grade_float = float(input("Input grade number {}: ".format(i+1)))
            value_grade_lst.append(grade_float)

        grades_dict[key_name] = value_grade_lst
        value_grade_lst = []

    return sorted(grades_dict.items())

def get_average (grades):
    '''Function takes in a dict and calculates avrage grades of the values '''
    average_list = []
    total = 0
    average = 0
    for key,value in grades:
        for grade in value:
            total += grade
        average = total / NUM_OF_GRADES
        total = 0
        average_list.append((key,average))
            
    return sorted(average_list)

def sort_largest (average_grades):
    return sorted(average_grades, key=operator.itemgetter(1), reverse=True)

def print_data (grades, avrage):
    print("Student list:")
    for name,grade in grades:
        print("{}: {}".format(name, grade))
    print("Student with highest average grade:")
    print("{} has an average grade of {:.2f}".format(avrage[0][0], avrage[0][1]))
    return

def main():
    student_grades = get_grades()
    average_grades = get_average(student_grades)
    average_grades_sorted = sort_largest(average_grades)
    print_data(student_grades, average_grades_sorted)
main()