RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3


def read_file ():
    ''' Biður um nafn á file , ef það finnst ekki skilar villuboði '''
    try:
        file_name = input("Enter filename: ")
        file_open = open(file_name, "r")
        return file_open
    except IOError:
        print("Filename",file_name ,"not found!")
        return None

def create_players_dict(filestream):
	players_dict = {}
	for line in filestream:
		rank, name, country, rating, byear = line.split(";")
		last_name, first_name = name.split(',')

		# Clear whitespaces from last and firstname
		first_name = first_name.strip()
		last_name = last_name.strip()
		country = country.strip()

		key = "{} {}". format(first_name, last_name)
		value = (int(rank), country, int(rating), int(byear))
		players_dict[key] = value

	return players_dict

def create_countries_dict(dict_players):
	country_dict = {}

	for player_name, player_data in dict_players.items():
		country = player_data[COUNTRY]
		if country in country_dict:
			name_list = country_dict[country]
			name_list.append(player_name)
		else:
			# initialize new list w. 1 name and add to dict
			country_dict[country] = [player_name]

	return country_dict

def create_byear_dict(dict_players):
	byear_dict = {}

	for player_name, player_data in dict_players.items():
		byear = player_data[BYEAR]
		if byear in byear_dict:
			name_list = byear_dict[byear]
			name_list.append(player_name)
		else:
			# initialize new list w. 1 name and add to dict
			byear_dict[byear] = [player_name]

	return byear_dict

def print_sorted(dict_countries, dict_player):
	sorted_dict = sorted(dict_countries.items())
	for key, players in sorted_dict:
		average_rating = get_average_rating(players, dict_player)
		print("{} ({}) ({:.1f})".format(key, len(players), average_rating))
		for player in players:
			rating = dict_player[player][RATING]
			print('{:>40}{:>10d}'.format(player, rating))
	return

def get_average_rating(players, dict_players):
	ratings = [ dict_players[player][RATING] for player in players]
	average = sum(ratings)/len(ratings)
	return average

def print_header(header):
	print(header)
	dashes = '-' * len(header)
	print(dashes)

# Main starts here
filestream = read_file()
if filestream:
	dict_player = create_players_dict(filestream)
	dict_countries = create_countries_dict(dict_player)
	print_header("Players by country:")
	print_sorted(dict_countries, dict_player)

	dict_byear = create_byear_dict(dict_player)
	print_header("Players by birth year:")
	print_sorted(dict_byear, dict_player)
