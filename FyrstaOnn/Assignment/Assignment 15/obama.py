def name_input ():
    name_str = input("Enter a name: ").lower()
    return name_str.split()
    

def comon_letters_list (name):
    comon_letters = []
    for char in name[0]:
        if char in name[1]:
            if char not in comon_letters:
                comon_letters.append(char)
    return comon_letters

def comon_letters_set (name):
    set_1, set_2 = set(name[0]), set(name[1])
    return set_1 & set_2

def main ():
    name = name_input()
    comon_list = comon_letters_list(name)
    comon_set = comon_letters_set(name)
    print(sorted(comon_list))
    print(sorted(comon_set))
    
main()