numbers = ['1', '5', '10', '8']
numbers2 = [5, 2, 3, 8]
union = numbers2
print(numbers, [int(x) for x in numbers])
numbers = [int(x) for x in numbers]
print(numbers)
#numbers = [x for x in numbers if x in numbers2]
print(numbers)
union = [x for x in numbers if x not in union]
print(union)