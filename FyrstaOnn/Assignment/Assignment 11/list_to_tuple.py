#list_to_tuple function goes here
def list_to_tuple (any_list):
    a_tuple = tuple()
    try:
        for element in any_list:
            a_tuple = a_tuple + (int(element),)
    except ValueError:
        a_tuple = tuple()
        print("Error. Please enter only integers.")
    return a_tuple


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)