# Your function definition goes here
def count_case(user_string):
    upper_count = 0
    lower_count = 0
    for char in user_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)
user_input = input("Enter a string: ")
# Call the function here
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)