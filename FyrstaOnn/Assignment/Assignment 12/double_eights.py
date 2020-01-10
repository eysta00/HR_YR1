def get_list ():
    number_list = []
    try:
        number_list = input("Enter elements of list separated by commas: ").split(',')
        number_list = [int(i) for i in number_list]
        return number_list
    except ValueError:
        print("Error - please enter only integers.")

def double_eights (num_list):
    position = 0
    try:
        position = num_list.index(8)
        try:
            if num_list[position + 1] == 8:
                return True
        except IndexError: # Ef áttan er seinasta talan
            return False
    except ValueError: # Ef það eru engar áttur
        return False

print(double_eights(get_list()))