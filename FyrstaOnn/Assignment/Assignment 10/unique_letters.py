import string

def unique_letter (user_input):
    uniques_list = []
    for char in user_input:
        if char not in uniques_list:
            if char not in string.punctuation:
                uniques_list.extend(char.strip())
    return uniques_list

# Main starts here
sentence = input("Input a sentence: ")
unique_letters = unique_letter(sentence)
# Call the function here
print("Unique letters:", unique_letters)
