#Eysteinn Örn Jónsson
#22/8/19

year = int(input("Years: "))
popu = 307357870
seconds = 365 * 24 * 60 * 60
deaths_year = seconds / 13
births_year = seconds / 7
immigr_year = seconds / 35
popu_new = 0
year_float = float(year)
if year >= 0:
    popu_new = ((births_year + immigr_year) * year_float + popu + (-1 * deaths_year * year_float))
    print ("New population after", year, "years is", int(popu_new))
else:
    print("Invalid input!")
