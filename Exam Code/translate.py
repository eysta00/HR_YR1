#       Markimið forrits er að þýða ákveðnar skammstafanir sem er notað í farsímaskilaboðum yfir í venjuleg orð.

# Tekur inn nafn á skrá.
#   Forrit býr til dictionary fyrir þær þýðingar.
#   símastytting (key) og þýðing (value)
# Forrit byður svo um skilaboð til að þýða.
# Forrit skilar orðinu þýtt.
import string
def read_file ():
    ''' Biður um nafn á file , ef það finnst ekki skilar engu '''
    try:
        file_name = input("Enter name of mapping file: ")
        file_open = open(file_name, "r")
        return file_open
    except IOError:
        return None

def ask_user_str():
    return input("Enter a message: ")

def make_translation_dict (filestream):
    '''Búið til þýðingar uppflettiskrá '''
    translation_dict = dict()
    for line in filestream:
        key, value = line.split(":")
        key, value = key.strip(), value.strip()
        translation_dict[key] = value
    return translation_dict

def translate_messasge (translation_dict, user_string):
    '''Þýðir skilaboðið sem notandi vill þýða með uppflettiskrá'''
    user_lst = user_string.split(" ")
    trans_msg = []
    for word in user_lst:
        sms_word = word.strip(string.punctuation)
        if sms_word in translation_dict:
            if word[-1] in string.punctuation: # Ef orðið er skammstöfun og endar með greinarmerki.
                sms_word_punct = str(translation_dict[sms_word]) + str(word[-1])
                trans_msg.append(sms_word_punct)
            else:
                trans_msg.append(translation_dict[sms_word])
        else:
            trans_msg.append(word)
    print(*trans_msg)

# Main Pogram starts here.
def main ():
    filestream = read_file()
    if filestream:
        trans_dict = make_translation_dict(filestream)
        user_str = ask_user_str()
        while user_str != "q":
            translate_messasge(trans_dict, user_str)
            user_str = ask_user_str()

main()