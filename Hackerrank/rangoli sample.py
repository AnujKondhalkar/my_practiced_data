Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='abcd'
>>> a=a+a[::-1]
>>> a
'abcddcba'
>>> a='abcd'
>>> a[::-2]
'db'
>>> a
'abcd'
>>> a[:1:-1]
'dc'
>>> a[1::-1]
'ba'
>>> a
'abcd'
>>> a[::-1].remove(0)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[::-1].remove(0)
AttributeError: 'str' object has no attribute 'remove'
>>> b=a[::-1]
>>> b
'dcba'
>>> a
'abcd'
>>> a[::-1][1::]
'cba'
>>> a
'abcd'
>>> a=a+a[::-1][1::]
>>> a
'abcdcba'
>>> l='-'.join(a)
>>> l
'a-b-c-d-c-b-a'
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['e', 'ed', 'edc', 'edcb', 'edcba']


--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
[::-1]

>>> n=5
>>> for i in range()
SyntaxError: invalid syntax
>>> l='abcd'
>>> for i in range(len(l)):
	print(i)

	
0
1
2
3
>>> for i in range(1,len(l)):
	print(i)

	
1
2
3
>>> l='abcde'
>>> for i in range(1,len(l)):
	print(i)

	
1
2
3
4
>>> l=[]
>>> l[1]='5'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l[1]='5'
IndexError: list assignment index out of range
>>> l[0]='5'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l[0]='5'
IndexError: list assignment index out of range
>>> l
[]
>>> l[0]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l[0]
IndexError: list index out of range
>>> a='a'
>>> a
'a'
>>> a[::-1][1::]
''
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['e', 'ede', 'edcde', 'edcbcde', 'edcbabcde']
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['c', 'cbc', 'cbabc']
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['g', 'gfg', 'gfefg', 'gfedefg', 'gfedcdefg', 'gfedcbcdefg', 'gfedcbabcdefg']
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['g', 'gfg', 'gfefg', 'gfedefg', 'gfedcdefg', 'gfedcbcdefg', 'gfedcbabcdefg']
Traceback (most recent call last):
  File "C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py", line 16, in <module>
    print('-'.joint(l3[i]))
AttributeError: 'str' object has no attribute 'joint'
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['g', 'gfg', 'gfefg', 'gfedefg', 'gfedcdefg', 'gfedcbcdefg', 'gfedcbabcdefg']
Traceback (most recent call last):
  File "C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py", line 16, in <module>
    print('-'.joint(l3[i]))
AttributeError: 'str' object has no attribute 'joint'
>>> a='a'
>>> '-'.join(a)
'a'
>>> l=['as']
>>> '-'.join(l[0])
'a-s'
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
['g', 'gfg', 'gfefg', 'gfedefg', 'gfedcdefg', 'gfedcbcdefg', 'gfedcbabcdefg']
g-f-g
g-f-e-f-g
g-f-e-d-e-f-g
g-f-e-d-c-d-e-f-g
g-f-e-d-c-b-c-d-e-f-g
g-f-e-d-c-b-a-b-c-d-e-f-g
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
g
g-f-g
g-f-e-f-g
g-f-e-d-e-f-g
g-f-e-d-c-d-e-f-g
g-f-e-d-c-b-c-d-e-f-g
g-f-e-d-c-b-a-b-c-d-e-f-g
>>> len(--------e--------)
SyntaxError: invalid syntax
>>> len('--------e--------')
17
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------g------
----g-f-g----
--g-f-e-f-g--
g-f-e-d-e-f-g
g-f-e-d-c-d-e-f-g
g-f-e-d-c-b-c-d-e-f-g
g-f-e-d-c-b-a-b-c-d-e-f-g
>>> len(l3[-1])
13
>>> len('g-f-e-d-c-b-a-b-c-d-e-f-g')
25
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
>>> for i in range(5,0,-1)):
	
SyntaxError: invalid syntax
>>> for i in range(5,0,-1):
	print(i)

	
5
4
3
2
1
>>> l3
['g', 'gfg', 'gfefg', 'gfedefg', 'gfedcdefg', 'gfedcbcdefg', 'gfedcbabcdefg']
>>> len(l3)
7
>>> for i in range(len(l3),-1):
	print(i)

	
>>> for i in range(len(l3),0):
	print(i)

	
>>> for i in range(len(l3),0,-1):
	print(i)

	
7
6
5
4
3
2
1
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
Traceback (most recent call last):
  File "C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py", line 19, in <module>
    print('-'.join(l3[i]).center((len(l3[-1])*2)-1, '-'))
IndexError: list index out of range
>>> len(l3)
7
>>> for i in range(len(l3),0,-1):
	print(i)

	
7
6
5
4
3
2
1
>>> i=2
>>> print('-'.join(l3[i]).center((len(l3[-1])*2)-1, '-'))
--------g-f-e-f-g--------
>>> print('-'.join(l3[6]).center((len(l3[-1])*2)-1, '-'))
g-f-e-d-c-b-a-b-c-d-e-f-g
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
------g-f-e-d-e-f-g------
----------g-f-g----------
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
--------g-f-e-f-g--------
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
Traceback (most recent call last):
  File "C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py", line 18, in <module>
    for i in range(len(l3)-2,0,0):
ValueError: range() arg 3 must not be zero
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
>>> l3.reverse()
>>> l3
['gfedcbabcdefg', 'gfedcbcdefg', 'gfedcdefg', 'gfedefg', 'gfefg', 'gfg', 'g']
>>> for i in range(len(l3)-2,0,-1):
	print(i)

	
5
4
3
2
1
>>> 
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
Traceback (most recent call last):
  File "C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py", line 18, in <module>
    for i in range(len(l3)-2,-1,0):
ValueError: range() arg 3 must not be zero
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
------------g------------
>>> 
==== RESTART: C:\Users\Anuj\Documents\Python Programs\alphabet rangoli.py ====
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
------------g------------
>>> 
>>> a=''
>>> 
