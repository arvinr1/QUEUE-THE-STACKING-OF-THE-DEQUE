from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__content = [None] * self.__capacity
    self.__front = None
    self.__back = None
    self.__size = 0
    
  def __str__(self):
    # This method runs in O(n^2) time because the for loop will iterate
    # once through every value in O(n) time and perform a string concatenation
    # in O(n) time, making the overall performance O(n^2).
    content = '['
    if self.__size == 0:
      return '[ ]'
    for i in range(self.__size):
      index = (self.__front + i) % self.__capacity
      content += " " + str(self.__content[index])
      if i < self.__size - 1:
        content += ','
    content += ' ]'
    return content
    
  def __len__(self):
    # This method runs in O(1), it simply returns an attribute of the deque.
    return self.__size

  def __grow(self):
    # This method runs in O(2n) time because it first doubles the number of values
    # in the deque and then iterates through them each once to sort them into
    # a new array.
    new_content = self.__content + [None] * self.__capacity
    self.__capacity = self.__capacity*2
    new_content[0] = self.__content[self.__front]
    for i in range(1, self.__size):
      new_content[i] = self.__content[(self.__front + 1) % self.__size]
      self.__front = (self.__front + 1) % self.__size
    self.__content = new_content
    self.__front = 0
    self.__back = self.__size - 1
    
  def push_front(self, val):
    # In the worst case (where self.__grow is called) this method will run
    # in O(n) time because self.__grow runs in O(n) time and the rest of the
    # method runs in O(1) time.
    if self.__size == self.__capacity:
      self.__grow()
    if self.__capacity == 1:
      self.__front = 0
      self.__back = 0
      self.__content[0] = val
    else:
      self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
      self.__content[self.__front] = val
    self.__size += 1

  def pop_front(self):
    # This method only visits and pops the front value and 
    # therefore runs in O(1) time.
    if self.__size == 0:
      return
    val = self.__content[self.__front]
    self.__content[self.__front] = None
    if self.__capacity == 1:
      self.__back = None
      self.__front = None
    else:
      self.__front = (self.__front + 1) % self.__capacity
    self.__size -= 1
    return val

  def peek_front(self):
    # This method simply returns the front value and runs in O(1) time.
    if self.__size == 0:
      return
    return self.__content[self.__front]

  def push_back(self, val):
    # In the worst case (where self.__grow is called) this method will run
    # in O(n) time because self.__grow runs in O(n) time and the rest of the
    # method runs in O(1) time.
    if self.__size == self.__capacity:
      self.__grow()
    if self.__capacity == 1:
      self.__content[0] = val
      self.__front = 0
      self.__back = 0
    else:
      self.__back = (self.__back + 1) % self.__capacity
      self.__content[self.__back] = val
    self.__size += 1

  def pop_back(self):
    # This method only visits and pops the back value and 
    # therefore runs in O(1) time.
    if self.__size == 0:
      return
    val = self.__content[self.__back]
    self.__content[self.__back] = None
    self.__size -= 1
    if self.__capacity == 1:
      self.__back = None
      self.__front = None
    else:
      self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
    return val

  def peek_back(self):
    # This method simply returns the back value and runs in O(1) time.
    if self.__size == 0:
      return
    else:
      return self.__content[self.__back]
