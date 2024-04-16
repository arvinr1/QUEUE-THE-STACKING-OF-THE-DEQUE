import sys # for sys.argv, the command-line arguments

def delimiter_check(filename):
  # This function is performs in O(n) time because it reads through
  # the file where n is the number of characters through the file, and
  # then iterates through each character n number of times.
  stack = []
  with open(filename, 'r') as file:
    content = file.read()
    for i in content:
      if i in '([{':
          stack.append(i)
      elif i == ')':
          if not stack or stack[-1] != '(':
              return False
          stack.pop()
      elif i == ']':
          if not stack or stack[-1] != '[':
              return False
          stack.pop()
      elif i == '}':
          if not stack or stack[-1] != '{':
              return False
          stack.pop()
  return not stack

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')
