class StringSet:
    def __init__(self, string):
        self.string = string.split(" ")
        self.__words = []
        
        for word in self.string:
            if word not in self.__words:
                self.__words.append(word)
        
        #self.__words

    def __str__(self):
        string_whole = ""
        for word in self.__words:
            string_whole += word
            string_whole += " "
        string_whole = string_whole.strip()
        return string_whole

    def size(self):
        return len(self.__words)
    
    def __add__(self,other):
        union_list = self.__words + other.__words
        string_whole = ''
        for word in union_list:
            string_whole += word
            string_whole += ' '
        return StringSet(string_whole)
    
    def find(self, word):
        if word in self.__words:
            return True
        else:
            return False
    
    def at(self, index):
        return self.__words[index]


def main():
    str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
    set1 = StringSet(str1)
    str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
    set2 = StringSet(str2)
    print("Set1:", set1)
    print("Set2:", set2)
    print("Set1 size:", set1.size())
    print("Set2 size:", set2.size())
    the_union = set1 + set2
    print("Union:", the_union)
    print("Union size:", the_union.size())

    query = StringSet('chocolate cream fish good rubbish')
    print("Query:", query)
    count = 0
    for i in range(query.size()):
        if the_union.find(query.at(i)):
            count += 1
    
    print("Query size:", query.size())
    print("Found in union:", count)

    set1 = StringSet('word1 word2 word3 word2 word1 word4')
    assert set1.find('word2') == True
    assert set1.find('word5') == False



main()