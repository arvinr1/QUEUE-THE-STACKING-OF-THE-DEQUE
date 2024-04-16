class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.__size = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.next = None
        self.__header.prev = None
        self.__trailer.prev = self.__header

    def __len__(self):
        # The big-oh performance is O(1) because it
        # simply returns an attribute of the list.
        return self.__size
            

    def append_element(self, val):
        # O(n) because it could iterate through all nodes
        # until the last one.
        new_element = self.__Node(val)
        if self.__header.next == self.__trailer:
            self.__header.next = new_element
            new_element.next = self.__trailer
            new_element.prev = self.__header
            self.__trailer.prev = new_element
        else:
            cur = self.__header
            shift = True
            while shift == True:
                if cur.next == self.__trailer:
                    shift = False
                else:
                    cur = cur.next
            cur.next = new_element
            new_element.prev = cur
            self.__trailer.prev = new_element
            new_element.next = self.__trailer
        self.__size += 1

    def insert_element_at(self, val, index):
        # O(n): although there are two for loops, they are not
        # nested inside of each other and therefore run sequentially
        # at O(n). In the worst case, the method will iterate until
        # it reaches the end of the list.
        new_element = self.__Node(val)
        if index >= self.__size or index < 0:
            raise IndexError
        else:
            cur = self.__header
            cur_a = self.__header
            for i in range(0,index):
                cur = cur.next
            for i in range (0,index+1):
                cur_a = cur_a.next
            new_element.next = cur_a
            new_element.prev = cur
            cur.next = new_element
            cur_a.prev = new_element
            self.__size += 1

    def remove_element_at(self, index):
        # Performance is O(n) because in the worst case, 
        # the method visits each node once.
        if index >= self.__size or index < 0:
            raise IndexError
        cur = self.__header.next
        for i in range(index):
            cur = cur.next
        skip = cur
        for i in range(1):
            skip.prev.next = skip.next
            skip.next.prev = skip.prev
        val_node = cur.val
        self.__size -= 1
        return val_node

    def get_element_at(self, index):
        # Big-oh performance is O(n) because the for loop will iterate
        # through every node in the worst case.
        if index >= self.__size  or index < 0:
            raise IndexError
        else:
            cur = self.__header
            for i in range(0,index+1):
                cur = cur.next
            val_node = cur.val
            return val_node


    def rotate_left(self):
        # Big-oh performance is O(n) because the while loop will iterate
        # through every node in the worst case.
        if self.__size == 0 or self.__size == 1:
            return
        cur = self.__header.next
        temp = cur.val
        while cur.next != self.__trailer:
            cur.val = cur.next.val
            cur = cur.next
        cur.val = temp

        
    def __str__(self):
        # O(n): method will traverse and produce a string
        # for every element in the list.
        string =  '['
        if self.__size == 0:
            return '[ ]'
        cur = self.__header.next
        for i in range(self.__size):
            if cur and cur != self.__trailer:
                string += " " + str(cur.val)
                if i != self.__size-1:
                    string += ","
                cur = cur.next
        string += ' ]'
        return string

    def __iter__(self):
        # O(1), this is simply setting an index.
        self.__iter_index = 0
        return self

    def __next__(self):
        # The big-oh performance of this is O(n), it will iterate
        # once through the entire list in the worst case.
        if self.__iter_index == self.__size:
            raise StopIteration
        else:
            cur = self.__header.next
            for _ in range(self.__iter_index):
                cur = cur.next
            self.__iter_index += 1
            return cur.val


    def __reversed__(self):
        # O(n), the while loop will iterate through the entire list
        # one time.
        new = Linked_List()
        if self.__size == 0:
            return new
        cur_index = self.__size - 1
        while cur_index >= 0:
            new.append_element(self.get_element_at(cur_index))
            cur_index -= 1
        return new

if __name__ == '__main__':
    # TESTS
    ll = Linked_List()
    # Testing appending to the list
    ll.append_element(5)
    ll.append_element(10)
    print(ll)
    print(len(ll))
    print(ll.__str__())
    
    # Testing insertion at valid index.
    ll.insert_element_at(7,1)
    print(ll)

    # Testing insertion at invalid index.
    try:
        ll.insert_element_at(100,100)
    except IndexError:
        print(ll)
    
    # Testing removal at valid index.
    element = ll.remove_element_at(1)
    print(element)
    print(ll)

    ll.append_element(15)
    print(ll)
    ll.remove_element_at(1)
    print(ll)
    ll.remove_element_at(0)
    ll.remove_element_at(0)
    print(str(ll))

    # Testing removal at invalid index.
    try:
        ll.remove_element_at(100) 
    except IndexError:
        print(len(ll))
        print(str(ll))

    # Testing reversed + rotate_left.
    ll.append_element(1)
    ll.append_element(2)
    ll.append_element(3)
    for val in ll:
        print(val)
    for val in reversed(ll):
        print(val)
    ll.rotate_left()
    print(ll)
