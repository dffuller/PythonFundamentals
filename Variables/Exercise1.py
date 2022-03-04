import doctest
#lists
def list_test_1():
  """
  lists are mutable
  >>> list_test_1()
  ([1, 9, 3], [1, 9, 3])
  """
  a = [1,2,3];b=a;b[1] = 9; 
  return (a,b)

def list_test_2():
  """
  >>> list_test_2()
  ([1, 2, 3], [4, 5, 6])
  """
  a = [1,2,3]; b=a; b=[4,5,6]
  return (a,b)

# ints
def int_test():
  """
  >>> int_test()
  (1, 2)
  """
  a=1; b=a; b=2
  return (a,b)
 
#floats
def float_test():
  """
  >>> float_test()
  (1.0, 2.0)
  """
  a = 1.0; b=a; b=2.0
  return (a,b)

#str
def str_test_1():
  """
  strings are immutable
  >>> str_test_1()
  Traceback (most recent call last):
      ...
  TypeError: 'str' object does not support item assignment
  """
  a = "hello"; b=a; b[0] = 'j'; print(a,b)
  return (a,b)
def str_test_2():
  """
  >>> str_test_2()
  ('hello', 'jello')
  """
  a = "hello"; b=a;b = "jello"
  return (a, b)

#tuples
def tuple_test_1():
  """
  tuples are immutable
  >>> tuple_test_1()
  Traceback (most recent call last):
      ...
  TypeError: 'tuple' object does not support item assignment
  """
  a = (1,2,3); b=a; b[0]=4
  return (a, b)
def tuple_test_2():
  """
  >>> tuple_test_2()
  ((1, 2, 3), (4, 5, 6))
  """
  a = (1,2,3); b=a; b=(4,5,6)
  return (a, b)  

# dictionaries
def dict_test_1():
  """
  >>> dict_test_1()
  ({'a': 3, 'b': 2}, {'a': 3, 'b': 2})
  """
  a = dict(a=1, b=2); b=a; b['a']=3
  return (a, b)
def dict_test_2():
  """
  >>> dict_test_2()
  ({'a': 2, 'b': 4}, {'a': 1, 'b': 2})
  """
  a = dict(a=1, b=2); b=a; a=dict(a=2,b=4)
  return (a, b)

if __name__ == "__main__":
  doctest.testmod()
