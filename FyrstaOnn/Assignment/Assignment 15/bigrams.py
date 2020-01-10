import string

def words_to_list(filestream):
    filestream = filestream.read()
    whole_list = []
    all_words = filestream.split()
    for word in all_words:
        new_word = ""
        for char in word:
            if char not in string.punctuation:
                new_word += char
        whole_list.append(new_word.lower())
    return whole_list

def tuple_biagram_list (words_list):
    biagram_list = []
    for i in range(len(words_list)-1):
        biagram_list.append((words_list[i],words_list[(i+1)]))
    return biagram_list

def word_list_to_counts (word_list):
    word_count_dict = {}
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

def main():
    file_name = input("Enter name of file: ")
    filestream = open(file_name, 'r')
    words = words_to_list(filestream)
    biagrams = tuple_biagram_list(words)
    diction = word_list_to_counts(biagrams)
    diction_list = []
    sorted_list = [(k, diction[k]) for k in sorted(diction, key=diction.get, reverse=True)]
    
    print(sorted_list[:10])

main()