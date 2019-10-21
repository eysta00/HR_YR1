# Forrit byður um 2x heiltölu inntök frá notanda sem eru aðgreind með bilum.
# Forrit býr til tvö mengi útfrá inntökunum og losar við endurtekningar
# forritið gerir sniðmengi útfrá hinum tvem mengunum og skilar því
# forritið gerir sammengi útfrá hinum tvem mengunum og skilar því
# *** In retrospect hefði kanski geta notað list comprihension ***

def user_inputs ():
    '''Tekur inn tvö inntök, breytir þeim í int og setur í lista og raðar'''
    user_input_1 = input("Enter elements of a list separated by space: ")
    user_input_2 = input("Enter elements of a list separated by space: ")
    user_list_1 = user_input_1.split()
    user_list_2 = user_input_2.split()
    user_set_1 = []
    user_set_2 = []
    user_set_1_int = []
    user_set_2_int = []
    for element in user_list_1: # Skoðað duplicates
        if element not in user_set_1:
            user_set_1.append(element)
    for element in user_list_2:
        if element not in user_set_2:
            user_set_2.append(element)
    
    for element in user_set_1: #Breytum frá strengi yfir í integer
        user_set_1_int.append(int(element))
    for element in user_set_2:
        user_set_2_int.append(int(element))
    
    user_set_1_int.sort()
    user_set_2_int.sort()
    return [user_set_1_int, user_set_2_int]

def intersection_set_creator (user_sets):
    '''Býr til lista yfir allar sameiginlegar tölur og raðar'''
    inters_set = []
    for element in user_sets[0]: # Skoðað allar sameiginlegar tölur
        if element in user_sets[0] and element in user_sets[1] and element not in inters_set:
            inters_set.append(element)
    return sorted(inters_set)

def union_set_creator (user_sets):
    '''Býr til lista yfir öll gildi og raðar'''
    union_set = []
    for element in user_sets[0]:
        if element not in union_set:
            union_set.append(element)
    for element in user_sets[1]:
        if element not in union_set:
            union_set.append(element)
    return sorted(union_set)

user_sets = user_inputs()
print("Set 1: {}\nSet 2: {}".format(user_sets[0],user_sets[1]))
print("Intersection:", intersection_set_creator(user_sets))
print("Union:", union_set_creator(user_sets))