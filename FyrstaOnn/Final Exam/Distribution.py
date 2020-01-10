class Distribution:
    def __init__(self, file_stream = None):
        
        self.__distribution = {}
        self.__file_stream = file_stream

        if type(file_stream) == dict: # Check for type (for __add__)
            self.__distribution = file_stream
        else:
            if self.__file_stream: # Count the numbers
                for line in self.__file_stream:
                    line = line.split()
                    line = [int(i) for i in line]
                    for num in line:
                        if num in self.__distribution:
                            self.__distribution[num] += 1
                        else:
                            self.__distribution[num] = 1
        
    def __str__(self):
        print_string = ""
        if self.__distribution:
            for key, value in sorted(self.__distribution.items()):
                print_string += "{}: {}\n".format(key, value)
            return print_string
        else:
            return ''

    def average(self):
        total = 0
        number_of_numbers = 0
        if self.__distribution:
            for key,value in self.__distribution.items():
                total += key * value
                number_of_numbers += value

            return total / number_of_numbers
        else:
            return 0
    
    def __add__(self, other):
        new_dict = {}
        
        for key,value in self.__distribution.items():
            new_dict[key] = value
        
        for key,value in other.__distribution.items():
            if key in new_dict:
                new_dict[key] += value
            else:
                new_dict[key] = value
        
        return Distribution(new_dict)
    
    def __ge__(self,other):
        return self.average() >= other.average()

    def set_distribution(self, distribution):
        self.__distribution = distribution