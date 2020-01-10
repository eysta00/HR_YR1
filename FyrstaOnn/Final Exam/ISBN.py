ISBN_DASH_POS = [1, 5, 11]
ISBN_LEN = 13

def get_user_input():
    ''' Asks user for an ISBN, if "q" is given return None '''
    user_str = str(input("Enter an ISBN: "))
    if user_str == "q":
        return None
    else:
        return user_str

def isbn_checker(user_str):
    ''' Checks if the ISBN is valid or not '''
    dashes_pos = []
    int_list_check = []
    if len(user_str) == ISBN_LEN:

        for i,c in enumerate(user_str):     # check if the posisitions
            if c == '-':                    # of dashes are correct
                dashes_pos.append(i)
        if dashes_pos == ISBN_DASH_POS:
            
            int_list_check = user_str.split("-")
            try:                            # check if numbers are numbers and not letters
                int_list_check = [int(i) for i in int_list_check]
                return True

            except ValueError:
                return False
        else:
            return False
    else:
        return False

def print_validity(isbn_bool):
    ''' Prints the status '''
    if isbn_bool:
        print("Valid format!")
    else:
        print("Invalid format!")


# Main starts here
user_str = get_user_input()
while user_str:
    print_validity(isbn_checker(user_str))
    user_str = get_user_input()