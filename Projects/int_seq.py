#29/8/19
#Eysteinn Orn Jonsson

#Breytur skilgreindar
num = 1
num_odd = 0
num_even = 0
num_max = 0
num_sum = 0


while num > 0:
    num = int(input("Enter an integer: ")) #User input
    if num > 0: #Summa talna reiknad
        num_sum += num
        print("Cumulative total:", num_sum)
    if num > num_max: #Skilgreina staerstu tolu
        num_max = num
    if num > 0:
        if num % 2 == 0: #Telja fjolda oddatolur og slettartolur
            num_even += 1
        else:
            num_odd += 1
if num_sum > 0:
    print("Largest number:", num_max)
    print("Count of even numbers:", num_even)
    print("Count of odd numbers:", num_odd)
