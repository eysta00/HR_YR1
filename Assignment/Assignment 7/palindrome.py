# palindrome function definition goes here
def palindrome(user_input):
    str_1 = user_input.strip()
    str_2 = user_input[::-1].strip()
    if str_1 == str_2:
        return True
    else:
        return False

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
if palindrome(in_str):
    print(in_str + "is a palindrome.")
else:
    print("\"" + in_str "\"is not a palindrome")