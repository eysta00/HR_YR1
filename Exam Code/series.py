"""
num_first = int(input("First: "))
num_step = int(input("Step: "))
num_sum = 0
for x in range(num_first, 100, num_step):
    print(x, end=' ')
"""
num_first = int(input("First: "))
num_step = int(input("Step: "))
num_sum = 0
while num_step >= 0 and num_sum < 100:
    print(num_first, end=' ')
    num_sum += num_first
    num_first += num_step
else:
    print("\nSum of series:", num_sum)
