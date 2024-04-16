import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # Deque Tests
  # Test pushing and popping with mixed data types
  def test_deque_mixed_data(self):
    self.__deque.push_front(10)
    self.__deque.push_back("end")
    self.assertEqual('[ 10, end ]', str(self.__deque))
    self.assertEqual("end", self.__deque.pop_back())
    self.assertEqual(10, self.__deque.pop_front())

  # Test popping from an empty deque
  def test_deque_pop_empty(self):
    self.assertIsNone(self.__deque.pop_front())
    self.assertIsNone(self.__deque.pop_back())

  # Stack Tests
  # Test pushing and popping with mixed data types
  def test_stack_mixed_data(self):
    self.__stack.push(10)
    self.__stack.push("top")
    self.assertEqual("top", self.__stack.pop())
    self.assertEqual(10, self.__stack.pop())

  # Test popping from an empty stack
  def test_stack_pop_empty(self):
    self.assertIsNone(self.__stack.pop())

  # Queue Tests
  # Test enqueuing and dequeuing with mixed data types
  def test_queue_mixed_data(self):
    self.__queue.enqueue(10)
    self.__queue.enqueue("next")
    self.assertEqual(10, self.__queue.dequeue())
    self.assertEqual("next", self.__queue.dequeue())

  # Test dequeuing from an empty queue
  def test_queue_dequeue_empty(self):
    self.assertIsNone(self.__queue.dequeue())

  # Additional Tests
  def test_large_data(self):
    for i in range(1000):
      self.__deque.push_front(i)
      self.__stack.push(i)
      self.__queue.enqueue(i)
    
    for i in reversed(range(1000)):
      self.assertEqual(i, self.__deque.pop_front())
      self.assertEqual(i, self.__stack.pop())
    
    for i in range(1000):
      self.assertEqual(i, self.__queue.dequeue())

if __name__ == '__main__':
  unittest.main()
