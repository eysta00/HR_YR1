def to_list(input_string):
    words_list = []
    new_string = input_string.split(",")
    seperator = ' '
    new_string = seperator.join(new_string)
    words_list = new_string.split(" ")
    return words_list

# The main program starts here
the_string = input("Enter the string: ")
the_list = to_list(the_string)
# call your function here
print(the_list)