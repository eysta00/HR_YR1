# Eysteinn Örn Jónsson
# 3/10/19 - Project 7 - Stock Prices

# Forrit tekur inntak frá notanda um hvaða skrá eigi að opna,
#   ef skrá finnst ekki sendir villuboð.
# Forrit reiknar út meðaltal virði hlutabréfa á öllum dögum sérhverjum mánuði 
#   og raðar því ásamt mánuðinum.
# 
# Forrit prentar meðalvirði hlutabréfa fyrir mánuði.
# Forrit prentar hæðsta gildi og daginn sem það var.

# Staðsetningar dálka skilgreint sem fastar
VOLUME = 6
ADJ_CLOSE = 5
DATE = 0

def read_file ():
    ''' Biður um nafn á file , ef það finnst ekki skilar villuboði '''
    try:
        file_name = input("Enter filename: ")
        file_open = open(file_name, "r")
        return file_open
    except IOError:
        print("Filename",file_name ,"not found!")
        quit()

def  get_data_list(file_input):
    ''' Tekur inn skráarstraum og setur gögnin í lista '''
    data_list = []
    formated_data_list = []
    file_input.readline() # Lesið og sleppt fyrstu línu
    for line in file_input:
        line = line.strip()
        line_list = line.split(",")

        formated_data_list.append(line_list[0]) # Upphafsgildið sett í lista

        line_list = line_list[1:]
        line_list = [float(i) for i in line_list] # Breytt í float

        formated_data_list.extend(line_list) # Restinn af gildum í línu sett í lista
        data_list.append(formated_data_list) # Sett í heildarlista
        formated_data_list = []
    
    return data_list

def get_monthly_avrages(data_list):
    ''' Finnur út meðaltal á 'adjusted close' í öllum mánuðum út frá gagnalista '''
    avrage_month = 0
    total_value = 0
    total_volume = 0
    curr_month = ""
    monthly_avrages = []
    for a_list in data_list:
        if curr_month == "": # Núllstilling breytt
            curr_month = a_list[DATE][:7]
        if a_list[DATE][:7] == curr_month: # Reiknað alla daga í mánuðinum
            total_value += (a_list[VOLUME] * a_list[ADJ_CLOSE])
            total_volume += a_list[VOLUME]
        else:
            monthly_avrages.append((curr_month,(total_value/total_volume)))
            total_value = (a_list[VOLUME] * a_list[ADJ_CLOSE]) # Upphafsstillt með fyrstu tölum næsta mánaðar
            total_volume = a_list[VOLUME]
            curr_month = a_list[DATE][:7] # Næsti mánuður stilltur
    
    monthly_avrages.append((curr_month,(total_value/total_volume))) # Seinasta stak set í listann
    return monthly_avrages



def get_highest_value_day(data_list):
    ''' Finnur hæðsta gildið af 'adjusted close' og skilar því ásamt dagsetninguni '''
    highest_value = []
    for a_list in data_list:
        highest_value.append((a_list[ADJ_CLOSE],a_list[DATE]))

    return max(highest_value)

def print_info (monthly_avrages_list, highest_value_and_day):
    ''' Prentar gögn fallega '''
    print("{:<10s}{:>7s}".format("Month","Price"))
    for a_tuple in monthly_avrages_list: # For-lykkja sem prentar út allar niðurstöður
        print("{:<10s}{:>7.2f}".format(a_tuple[0],a_tuple[1]))
    print("Highest price {:.2f} on day {}".format(highest_value_and_day[0],highest_value_and_day[1]))

def main ():
    file_stream = read_file()
    data_list = get_data_list(file_stream)
    monthly_avrages_list = get_monthly_avrages(data_list)
    highest_value_and_day = get_highest_value_day(data_list)
    print_info(monthly_avrages_list,highest_value_and_day)

main()