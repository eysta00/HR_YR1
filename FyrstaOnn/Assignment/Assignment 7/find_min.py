# find_min function definition goes here
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
def find_min(num_1,num_2):
    if num_1 < num_2:
        num_smaller = num_1
    else:
        num_smaller = num_2
    return num_smaller

minimum = find_min(first,second) # Call the function here
print("Minimum: ", minimum)