#Eysteinn Örn Jónsson
#16/9/2019 Project 4. move.py

"""
Byður notenda um:
    1. staðsetningu sem á að vera á millibilinu 1 og 10.
    2. prentar streng sem hefur 9 x stök og eitt o stak sem á 
        að vera í staðsetninguni sem var beðið um.
    3. prentar út leiðbeiningar sem segja notenda hvernig á að hreyfa
        "o" til vinstri (l:left) og hægri (r:right), ásamt hvernig á að hætta. 
byður um inntak og á meðan inntakið er l eða r þá
    l á að færa "o" til vinstri um eitt stak og r færir "o" til hægri um eitt stak.
    - ekki á að færa staðsetningu ef o er í einum og inntak er l
    - ekki á að færa staðsetningu ef o er í tíu og inntak er r
    eftir að inntak er valið þá á að prenta strenginn út með viðeigandi breytum.
"""
# Breytur skilgreindar
MAX_X = 10
MIN_X = 1
posistion_input = 1
display_string = "xxxxxxxxxx"
print_string = display_string

# Fallið move skilgreint - heldur um staðsetningu á "o" og silar því.
def move (direction, posistion):
    if direction == "r" and posistion < MAX_X:
        posistion += 1
    elif direction == "l" and posistion > MIN_X:
        posistion -= 1
    return posistion

# Fallið print_position skilgreint - fallið prentar út streng og breytir staðsetningu á "o" í strengum
def print_position (posistion):
    
    print_string = display_string[:posistion_input - 1] + 'o' + display_string[posistion_input:]
    print(print_string)
    return


posistion_input = int(input("Input a position between 1 and 10: "))
print_position(posistion_input)
print("l - for moving left\nr - for moving right\nAny other letter for quitting")# leiðbeiningar eru birtar á skjáinn
direction_input = str(input("Input your choice: "))

while direction_input == "r" or direction_input == "l": # leyfileg gildi skilgreind

    posistion_input = move(direction_input, posistion_input) # Move fallið keyrt

    print_position(posistion_input) # print_position fallið keyrt

    direction_input = str(input("Input your choice: ")) # Endað með að spyrja hvaða átt á að færa "o" í.
else:
    print_position(posistion_input)