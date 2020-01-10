class Bug:
    def __init__(self, inital_pos = 1):
        self.i_pos = inital_pos
        self.__bug_str_len = 20

        if self.i_pos > self.__bug_str_len:
            self.i_pos = self.__bug_str_len
        elif self.i_pos < 1:
            self.i_pos = 1

        self.__move_dir = 1

        

    def __str__(self):
        '''Prentar leiðina hjá pöttu'''
        bug_string = ""
        for i in range(1, self.__bug_str_len + 1):
            if i == self.i_pos:
                bug_string += "b"
            else:
                bug_string += "x"
        return bug_string


    def move(self):
        '''Færir pöttuna um einn nema þegar hún er á endanum eða á bryjun '''
        self.i_pos += self.__move_dir
        
        # Skoðað hvort það sé á enda eða byrjun.
        if self.i_pos > self.__bug_str_len:
            self.i_pos = self.__bug_str_len
        elif self.i_pos < 1:
            self.i_pos = 1

    def turn(self):
        '''Breytir um átt pöttu'''
        self.__move_dir = self.__move_dir * -1

    def __gt__(self, other):
        '''Ber saman hvort ein patta hefur ferðast lengra en önnur '''
        if self.i_pos > other.i_pos:
            return True
        else:
            return False

    def __add__(self, other):
        '''Býr til nýja pöttu með samanlögðu leiðangrum hjá tvem pöttum '''
        return Bug(self.i_pos + other.i_pos)
