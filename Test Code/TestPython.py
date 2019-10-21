a_list = [3, 4, 5] + [6]
b_list = [3, 9]*2
result_list = []

for i, value in enumerate(a_list):
   value_to_append = value
   if b_list[i] > value:
       value_to_append = b_list[i]
   result_list.append(value_to_append)
print (a_list)
print(result_list)
