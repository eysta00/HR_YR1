'''
    1. Request an int from user.
    2. In a while loop have the user int compares to the max number.
    3. If the user int is smaller than the max int, ask again.
    4. If the user int is bigger than the max int, make it the new max int.
    5. If the user int is a negative number, then end the program.
'''

num_int = int(input("Input a number: "))
max_int = 1
while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
        num_int = int(input("Input a number: "))
    else:
        num_int = int(input("Input a number: "))

print("The maximum is", max_int)
