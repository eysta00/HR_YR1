'''
1. The length of the sequence is asked, but it has to be longer than 3
2. first three numbers are added to a sum.
3. The next three numbers are added to a sum.
4. And every subseqent three numbers are added to a sum to make the next number.
'''

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num1 = 1
num2 = 2
num3 = 3
num_sum = 0
for i in range(1,n+1):
    if i <= 3:
        print (i)
    else:
        num_sum = (num1 + num2 + num3)
        num1, num2, num3 = num2, num3, num_sum
        print(num_sum)