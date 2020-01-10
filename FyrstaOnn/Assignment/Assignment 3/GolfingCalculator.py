hole = 1
par = 0
score = 0

while hole < 19:
    par = int(input("Par of hole "+str(hole)+": "))
    score = int(input("Score on hole "+str(hole)+": "))
    if par < 3 or score == 0:
        print ("invalid score")
    elif score == par - 3:
        print ("albatross")
    elif score == par - 2:
        print ("eagle")
    elif score == par - 1:
        print ("birdie")
    elif score == par:
        print ("par")
    elif score == par + 1:
        print ("bogey")
    elif score == par + 2:
        print ("double bogey")
    elif score == par + 3:
        print ("triple bogey")
    elif score > par + 3:
        print ("bad hole")
    hole += 1
