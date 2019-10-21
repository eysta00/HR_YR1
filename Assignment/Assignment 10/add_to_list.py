# Your functions should appear here

def ask_user ():
    user_input = input("Enter value to be added to list: ")
    return user_input

def print_else (user_list):
    for i in user_list:
        print(i)
    for i in user_list:
        print(i)
    for i in user_list:
        print(i)
    return
# Main program starts here
x = ask_user()
user_list = []
while x != "exit":
    user_list.append(x)
    x = ask_user()
else:
    print_else(user_list)


'''
user_input = input("Enter value to be added to list: ")
user_list = []

while user_input != "exit":
    user_list.append(user_input)
    user_input = input("Enter value to be added to list: ")
else:
    for i in user_list:
        print(i)
    for i in user_list:
        print(i)
    for i in user_list:
        print(i)
'''
# It should mostly be a sequence of function calls