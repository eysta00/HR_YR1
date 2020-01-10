#Eysteinn Örn Jónsson
#9.9.2019

"""
Fyrsti partur.

Fyrir allar tveggja stafa tölur
    lagt er saman einstakra tölustafi í töluni,
    reiknað er summa einstakra tölustafana og sett í annað veldi
    ef summan í öðru veldi er jafnt og talan
    þá á að skila töluni.


Annar partur.

Fyrir allar tölur,x, sem eru á milli 1 og 100
    finnið alla deila sem ganga upp í töluna x
    ef fjöldi talna sem gengur upp í töluna x
    er jafnt og 10 þá skal skila töluni x.
"""

# Breytur skilgreindar.
num_fyrst = 0
num_second = 0
num_result = 0
num_sqr = 0
counter = 0

# Skoðar summu einstakra tölustafi í tölu, setur 
# summuna í annað veldi og borið saman við töluna.
for i in range(10 ,100):
    # Skipti i upp í tvo hluta.
    num_fyrst = (i // 10) 
    num_second = (i % 10)
    # Legg hlutana saman og set í annað veldi.
    num_result = (num_fyrst + num_second) ** 2
    if i == num_result:
        print (i)

# Skoðað allar tölur sem hafa 10 deila.
for x in range(1,100):
    counter = 0
    # Skoðað alla deila sem ganga upp í x
    for l in range(1, x + 1):
        if x % l == 0:
            counter += 1
    if counter == 10:
        print(x)

