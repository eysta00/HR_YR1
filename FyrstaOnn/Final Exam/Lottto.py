LEN_OF_NUMS = 5
MAX_VAL = 40
MIN_VAL = 0

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def get_user_numbers():
    ''' Gets numbers from user and returns a list of numbers '''
    user_num = input("Enter winning numbers: ")
    user_lst = user_num.split()
    return user_lst

def check_number_validity(user_numbers):
    ''' Checks if user input was valid or not and returns True / False '''
    bool_var = False
    try:
        user_numbers = [int(i) for i in user_numbers]
    except ValueError:
        return False
    
    if len(user_numbers) == LEN_OF_NUMS:
        for num in user_numbers:
            if num <= MAX_VAL and num >= MIN_VAL:
                bool_var = True
            else:
                return False
    else:
        return False
    
    return bool_var


def print_correct_numbers(user_numbers, file_stream):
    ''' Takes in the lotto numbers and user numbers and marks the similarities '''
    winning_lst = []
    pos = 0
    for line in file_stream:
        line = line.split()
        winning_lst.append(line)
    
    for lotto in winning_lst: # Marking numbers if ther are any
        for num in user_num:
            if num in lotto:
                pos = lotto.index(num)
                row = winning_lst.index(lotto)
                winning_lst[row][pos] = winning_lst[row][pos] + "*"
    
    for row in winning_lst: # printing 
        print(*row)
                
    
# Main starts here
filename = input("Enter file name: ")
file_stream = open_file(filename)
if file_stream:
    user_num = get_user_numbers()
    if check_number_validity(user_num):
        print_correct_numbers(user_num, file_stream)
    else:
        print("Winning numbers are invalid!")
else:
    print("File {} not found!".format(filename))
