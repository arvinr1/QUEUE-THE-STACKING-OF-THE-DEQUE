from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # O(n), the str method will have to loop through the entire queue.
    return str(self.__dq)

  def __len__(self):
    # O(1), this method simply fetches an attribute.
    return len(self.__dq)

  def push(self, val):
    # Since the push_front method in the Array Deque performs in linear
    # time in its worst case, this function also performs in O(n) time.
    self.__dq.push_front(val)

  def pop(self):
    # O(1), this method only visits the first index.
    return self.__dq.pop_front()

  def peek(self):
    # O(1), this method only vists the first index.
    return self.__dq.peek_front()


# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
