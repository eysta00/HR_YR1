''' Write a program that asks for name from the user and then asks for a number and stores 
the two in a dictionary as key-value pair.
The program then asks if the user wants to enter more data (More data (y/n)? ) and 
depending on user choice, either asks for another name-number pair or exits.  Finally, it stores the 
dictionary key, values in a list of tuples and prints a sorted version of the list.
Note: If a name is already in the dictionary, the old value should be overwritten.'''

more_data = 'y'
contacts_dict = {}
contacts_list = []
while more_data == 'y':
    name = input("Name: ")
    number = input("Number: ")
    contacts_dict[name] = number
    more_data = input('More data (y/n)? ').lower()
else:
    for item in contacts_dict.items():
        contacts_list.append(item)
    contacts_list.sort()
    print(contacts_list)