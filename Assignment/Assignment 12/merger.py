
def merge_lists (list_1, list_2):
    merged_list = list_1 + list_2
    unique_list = []
    
    for element in merged_list:
        if element not in unique_list:
            unique_list.append(element)

    return sorted(unique_list)
    
# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
