# Forrit byður um skráarheiti
# Forrit telur fjölda orða í skrá þar sem greinarmerkji teljast sem sitt eigið orð
# Forrit skilar fjölda orða

def read_file_input ():
    try:
        file_name = input("Enter filename: ")
        open_file = open(file_name, "r")
        return open_file
    except IOError:
        print("File",file_name ,"not found!")
        quit()

def count_words (read_file_input):
    word_list = []
    punctuation_counter = 0

    for line in read_file_input:
        line_list = line.split()
        for element in line_list:
            word_list.append(element)
            if element[-1] == "." or element[-1] == "!" or element[-1] == "," or element[-1] == "?":
                punctuation_counter += 1
        
    print(word_list)
    return (len(word_list) + punctuation_counter)

data = read_file_input()
print(count_words(data))