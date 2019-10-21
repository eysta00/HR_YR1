# is_prime function definition goes here
def is_prime(number):
    if number > 1:
        prime_counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                prime_counter += 1
    
        if prime_counter == 2:
            return(True)
    else:
        return(False)

num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
if is_prime(num):
    print (num, "is a prime")
else:
    print (num, "is not a prime")