#Eysteinn Örn Jónsson
#Population.py - 29/9/19

#   Alrím
# Forritið byður um nafn á skrá sem inniheldur:
#   Fylki og dálk fyrir íbúafjöldan í lok hvers árs.
# Forrit spyr notanda um hvaða ár hann vill skoða.
# Forrit skilar minnsta íbúarfjölda ásamt hvaða ríki það var í
# Forrit skilar stærsta íbúarfjölda ásamt hvaða ríki það var í

def read_file ():
    '''Byður um skráarheiti, ef það finnst ekki skilar ERROR og stoppar,
    ef það finnst skrá, skilar "open_file" '''
    try:
        file_name = input("Enter filename: ")
        population_file_open = open(file_name, "r")
        return population_file_open
    except IOError:
        print("Filename",file_name ,"not found!")
        quit()
    
def ask_year (population_file):
    '''Spyr notanda um ártal, það er svo skoðað hvort það sé í skráni
    ef það er ekki þá er byrt "invalid input" og spurt aftur, ef það er í skránni
    þá er skilar fallið heiltölu sem merkir staðsetningu í lista'''
    first_line = population_file.readline()
    first_line_list = first_line.split()
    invalid_year = True
    while invalid_year: # Input breytt í streng fyrir index skipun að neðan.
        year_input = str(input("Enter year: "))
        if year_input in first_line_list:
            invalid_year = False
            return int(first_line_list.index(year_input))
        else:
            print("Invalid year!")

def create_population_list (population_file, year_input):
    '''býr til lista af túplum sem út frá ártalinu sem notandi valdi sem inniheldur
    íbúarfjölda ríkja: (íbúarfjöldi, ríki).'''
    line_list = []
    population_year = []

    for line in population_file:
        line_list = line.split()   

        if not line_list[1].isdigit():  # Tengi saman nöfnin sem eru 
                                        # tvö orð sem eitt element
            line_list[0:2] = [' '.join(line_list[0:2])]

        population_year.append((int(line_list[year_input]),line_list[0]))
    return population_year

def main ():
    population_file = read_file()
    user_input_year = ask_year(population_file)
    population_list = create_population_list(population_file, user_input_year)

    print("Minimum:", min(population_list))
    print("Maximum:", max(population_list))

main()