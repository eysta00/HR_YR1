# sort_list() function goes here
def sort_list(some_list):
    some_list.sort()
# get_list() function goes here
def get_list():
    number_list = []
    number = 0
    try:
        while True:
            number = int(input())
            number_list.append(number)
    except ValueError:
        return number_list
# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()