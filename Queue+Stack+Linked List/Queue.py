from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # This method performs in O(n) time, it must iterate through
    # the entire stack.
    return str(self.__dq)

  def __len__(self):
    # O(1) time, simply returning an attribute.
    return len(self.__dq)

  def enqueue(self, val):
    # This method performs in O(n) time in the worst case because
    # push_back performs in O(n) time in the worst case.
    self.__dq.push_back(val)

  def dequeue(self):
    # This method performs in O(1) time because it only vists
    # the first index.
    return self.__dq.pop_front()

  def peek(self):
    # This method performs in O(1) time because it only vists
    # the first index.
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
