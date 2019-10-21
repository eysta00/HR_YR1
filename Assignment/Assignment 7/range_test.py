# The function definition goes here
def range_test(number):
    if number > 1 and number < 555:
        return True
    else:
        return

num = int(input("Enter a number: "))

# You call the function here
if range_test(num):
    print(num, "is in range.")
else:
    print(num, "is outside the range!")