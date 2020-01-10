def menu_selection():
    print("Menu: ")
    selection = input("add(a), remove(r), find(f): ").lower()
    return selection

def add_to_dict(any_dict):
    add_key = input("Key: ")
    add_value = input("Value: ")
    if add_key not in any_dict:
        any_dict[add_key] = add_value
    else:
        print("Error. Key already exists.")

def remove_from_dict(any_dict):
    remove_key = input("key to remove: ")
    if remove_key in any_dict:
        del any_dict[remove_key]
    else:
        print("Key not found.")

def find_key_in_dict(any_dict):
    find_key = input("Key to locate: ")
    if find_key in any_dict:
        print("Value: ", any_dict[find_key])
    else:
        print("Key not found.")

def execute_selection(choice ,any_dict):
    if choice == "a":
        add_to_dict(any_dict)
    elif choice == "r":
        remove_from_dict(any_dict)
    elif choice == "f":
        find_key_in_dict(any_dict)
    return any_dict

def dict_to_tuples(any_dict):
    dict_list = []
    for item in any_dict.items():
        dict_list.append(item)
    return dict_list



# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()