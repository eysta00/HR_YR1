import string

def read_file ():
    ''' Biður um nafn á file , ef það finnst ekki skilar villuboði '''
    try:
        file_name = input("Enter filename: ")
        file_open = open(file_name, "r", encoding="utf-8")
        return file_open
    except IOError:
        print("Filename",file_name ,"not found!")
        return None

def paragraph_reader (filestream):
    paragraph_list = []
    line_list = []
    word_list = []
    a_list = []
    text_file_string = filestream.read()
    paragraph_list = text_file_string.split("\n\n")
    for paragraph in paragraph_list:
        line_list = paragraph.split("\n")
        for line in line_list:
            words = line.split(" ")
            for word in words:
                word = word.strip(string.punctuation)
                word_list.append(word)
        a_list.append(word_list)
        word_list = []

    return a_list

def word_count ():
    return

def top_10_words ():
    return

def top_20_words ():
    return

def print_data ():
    return

# Main starts here

filestream = read_file()
if filestream:
    paragraph_list = paragraph_reader(filestream)
    print(paragraph_list)
