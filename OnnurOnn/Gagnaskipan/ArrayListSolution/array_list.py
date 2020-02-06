class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class NotFound(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.is_ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index > self.size or index < 0:
            raise IndexOutOfBounds()
        if self.size >= self.capacity:
            self.resize()
        i = self.size
        while(i > index):
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[index] = value
        self.size += 1
        if self.size > 1:
            self.is_ordered = False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index >= 0 and index < self.size:
            self.arr[index] = value
            if self.size > 1:
                self.is_ordered = False
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(0)

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.size > index and index >= 0:
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.get_at(self.size - 1)

    #Time complexity: O(n) - linear time in size of list (but doesn't change time complexity of append or insert)
    def resize(self):
        tmp_arr = [0] * self.capacity * 2
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr
        self.capacity *= 2

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.size > index and index >= 0:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i + 1]
            self.size -= 1
            if self.size <= 1:
                self.is_ordered = True
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.is_ordered = True

    #Time complexity: O(1) - constant time
    def swap_adjacent(self, index):
        tmp = self.arr[index]
        self.arr[index] = self.arr[index - 1]
        self.arr[index - 1] = tmp
        self.is_ordered = False

    def float_down_recur(self, swap_index):
        if swap_index >= 1 and self.arr[swap_index] < self.arr[swap_index - 1]:
            self.swap_adjacent(swap_index)
            self.float_down_recur(swap_index - 1)

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if self.is_ordered == False:
            raise NotOrdered()
        else:
            self.append(value)
            self.float_down_recur(self.size - 1)
            self.is_ordered = True

    #Time complexity: O(log n) - logarithmic time in size of list
    # binary search
    def binary_search(self, value, left, right):
        if left == right:
            raise NotFound()
        index = (left + right) // 2
        if self.arr[index] == value:
            return index
        elif value < self.arr[index]:
            return self.binary_search(value, left, index)
        else:  #value > self.arr[index]
            return self.binary_search(value, index + 1, right)

    #Time complexity: O(n) - linear time in size of list
    # because it's a simple linear search
    def linear_search(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        raise NotFound()

    #Time complexity dependant on whether list is ordered
    def find(self, value):
        if self.is_ordered:
            return self.binary_search(value, 0, self.size)
        else:
            return self.linear_search(value)

    #Time complexity: O(n) - linear time in size of list
    # because it uses the linear search, then remove at,
    # both of which are O(n)
    def remove_value(self, value):
        # try:
        self.remove_at(self.find(value))
        # NotFound() raised in self.find will simply continue out of this operation
        # except NotFound:
        #     raise NotFound()
        # This is already in remove_at:
        # if(self.size <= 1):
        #     self.is_ordered = True
