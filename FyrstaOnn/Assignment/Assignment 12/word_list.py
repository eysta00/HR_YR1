import string

def read_file ():
    ''' Biður um nafn á file, ef það finnst ekki skilar villuboði '''
    try:
        file_name = input("Enter filename: ")
        file_open = open(file_name, "r")
        return file_open
    except IOError:
        print("Filename",file_name ,"not found!")

def unique_word_list (file_open):
    ''' Fjarlægir greinarmerkji frá orðum og skilar röðuðum einstökum orðum '''
    unique_word_list = []
    for line in file_open: # Sett öll orð í lista
        line_list = line.split()
        line_list = [word.strip(string.punctuation) for word in line_list] # Fjarlægt greinarmerkji
    
        for element in line_list: # Flokkað einstök orð
            if element not in unique_word_list:
                unique_word_list.append(element)

    unique_word_list.sort()
    return unique_word_list
    
print(unique_word_list(read_file()))