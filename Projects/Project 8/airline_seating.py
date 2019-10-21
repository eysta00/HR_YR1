# Eysteinn Örn Jónsson
# 14/10/19 - airline_seating.py

# Forrit tekur inntak frá notanda um fjöldi raða og fjölda sæta.
# Forrit prentar svo út öll sætin merkt með starfi og raðir merkt með tölum.
#    Þar sem það er alltaf bara einn gangur.

# Forrit biður svo notanda að taka frá röð og sæti.
#    Ef sætið er tekið þá prentast villumelding um að sætið er tekið og biðið aftur um röð og sæti.
#    Ef sætið er ekki til þá prentast villumelding um að sætið er ekki til og biðið aftur um röð og sæti.
# Forrit prentar svo sætin og raðirnar aftur en með X á sætinu sem notandinn valdi.
#   Forrit spyr svo hvort notandi vilja taka frá aftur, ef já þá endurtaka tvær línur að ofan.

# **Raðir og sæti á að útfæra sem lista af listum.**

import string
import copy # For deep copy

def get_seats():
    '''Asks for number of seats in airline and returns it as an integer'''
    return int(input("Enter number of seats in each row: "))

def get_rows():
    '''Asks for number of rows in airline and returns it as an integer'''
    return int(input("Enter number of rows: "))

def get_seating_list(seats_num,rows_num):
    '''Creates a list of lists according to airplane setup'''
    seatings_list = []
    airline_seats = []
    for i in range(rows_num):
        # create a alpahetical seating list
        for i in range(seats_num):
            seatings_list.append(string.ascii_uppercase[i])
        airline_seats.append(seatings_list)
        seatings_list = []
    return airline_seats

def print_seating(reservations):
    '''Prints the airline seating with a walk path in the middle and the number of rows. '''
    counter = 1

    for element_list in reservations:
        walk_path = len(element_list)//2
        print("{:>2}  ".format(counter),*element_list[:walk_path] ," ", *element_list[walk_path:],"")
        counter += 1

def make_deep_copy(any_list):
    '''Creates a Deep Copy to compare with occupied seats '''
    return copy.deepcopy(any_list)

def get_occupied_seat(airline_seatings, reservations):
    '''Asks user for a seat and reserves the seat in reservations list'''
    seat_number = input("Input seat number (row seat): ")
    row, seat = seat_number.split()
    
    try:
        row = int(row) - 1
        selected_row = airline_seatings[row]
        selected_seat = selected_row.index(seat)
        reservation_row = reservations[row]

        if reservation_row[selected_seat] == "X":
            print("That seat is taken!")
            get_occupied_seat(airline_seatings, reservations)
        else:
            reservation_row[selected_seat] = "X"
    except:
        print("Seat number is invalid!")
        get_occupied_seat(airline_seatings, reservations)

    return reservations
    
def available_seats(reservations):
    '''Checks if all seats are reserved, returns true or false'''
    for seat_row in reservations:
        for seat in seat_row:
            if seat != "X":
                return True
    return False

def main():
    rows_num = get_rows()
    seats_num = get_seats()
    airline_seating = get_seating_list(seats_num,rows_num)
    print_seating(airline_seating) #Inital Printing of airplane setup

    reservations = make_deep_copy(airline_seating) # Make a copy of airplane setup for reservations.

    answer = "y" # Main loop
    while answer == "y":
        reservation_seating = get_occupied_seat(airline_seating,reservations)
        print_seating(reservations)
        if available_seats(reservations):
            answer = input("More seats (y/n)? ")
        else:
            answer = "n"

main()