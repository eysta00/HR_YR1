def make_sets ():
    user_input = input("Input a list of integers separated with a comma: ")
    user_list = user_input.split(',')
    user_list = [int(i) for i in user_list]
    return set(user_list)

def intersection(set1, set2):
    return set1 & set2

def union(set1, set2):
    return set1 | set2

def difference(set1, set2):
    return set1 - set2

def menu_select (set1, set2):
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")

    set_oper = int(input("Set operation: "))
    if set_oper == 1:
        print(intersection(set1, set2))
    elif set_oper == 2:
        print(union(set1, set2))
    elif set_oper == 3:
        print(difference(set1, set2))
    else:
        quit()
        
def main():
    set_1 = make_sets()
    set_2 = make_sets()
    print(set_1)
    print(set_2)
    while True:
        menu_select(set_1, set_2)

main()