# Python Basics

#  Variables
# Variable name should begin with an alphabet or an underscore. You can have numbers after the first character. They
# are case sensitive, meaning that XYZ is different than xyz. Reserved words cannot be used as variables names
x = 100
X = 101
print(x)
print(X)

# Data Types:
# In numbers, there are 2 types, one without decimal referred to  as integer and the other which is Float
# and Double
# Then there also exists called as String (Collection of characters)
print(type(x))  # As you can see in the output it is showing that the class of the variable x having value 100 is 'int'

print()  # Ignore , this is for space in output

pi = 3.14
print(pi)
print(type(pi))  # Same here you can see that it is showing the class as Float

print()  # Ignore , this is for space in output

str = "Amaan Hasware"
print(str)
print(type(str))  # It will show as string

print()  # Ignore , this is for space in output

# Then comes the topic of list
#  A list is nothing but collection of values
# With Lists, a variable can have multiple values

list1 = [14, 67, 9]
print(list1)
print(type(list1))  # It will show as List

print()

# Lists can also store/have different data types
list1 = [1, 2, "Three"]
print(list1)  # It will show as List

#  If you want to extract a particular value from lists, you can call out the index number  (Starts from 0)
print(list1[1])

print(list1[0])

#  we can also change (add/remove the values)
list1[1] = 1.5
print(list1)  # here it changed the value of list1's value from 2 to 1.5 having the index number 1

print()

# Same as lists we also have tuples, but the syntax is with paranthesis '( )' & having some different qualties that
# we will study later

tupe1 = (4, 8, 6)
print(tupe1)
print(type(tupe1))  # it will show as the <class 'tuple'>

# The main difference between tuples and lists are that they are immutable . meaning that they cannot be changed
# You can access the values of tuples in the same way as you do for lists

print(tupe1[0])  # it will give the value of 0th index number of the tuple 'tupe1'

print()

# Arithmetic Operations
a = 20
b = 30
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # will give value in int not in float
print(a % b)  # will give remainder

print()

# String Operations
var = "Amaan Hasware"
print(var)
# Accessing elements  of a String
print(var[0])
# To Access the range of elements we use ':'
print(var[0:4])
# You can also get it from behind
print(var[4:])  # Not specifying the initial starting range will default set it to 0 (beginning to the specified last
# index value) and vice versa if not mentioned the last(ending range)

print()

# Python Numbers
num = 5
print(num)
print(type(num))

num = 5.4
print(num)
print(type(num))

#  You can also have imaginary numbers
numI = 5 + 2j
print(numI)
print(type(numI))  # it will print out as Complex

# to only print real part, you use the keyword 'real'
print(numI.real)
print(type(numI))

# same for imaginary part, use the keyword 'imag'
print(numI.imag)
print(type(numI))

print()

# you can also concatenate(add)  variables
A = 'Amaan'
H = "Hasware"
print(A + H)

print()

# Conversions
# Any vale present between the quotes of a string makes it a string
x = '192'
print(x)
print(type(x))  # It will show string

print()

# To convert the vaalues from string to int or from any other , here is the syntax
# new/old_variable)name = Designated_data_type(variable_name)
# Eg:
# Let's convert the above-mentioned string into int
x1 = int(x)
print(x1)
print(type(x1))
#  let's convert it into complex

print()

x2 = complex(x1)
print(x2)
print(type(x2))

print()

#  we can also print complex numbers using the keyword complex
print(complex(2, 5))

print()

# Functions (in-built)
# 1) abs - it will always return the positive value of rhe variable it is being called out to
x1 = -12
print(abs(x1))

print()
import math

x = 10
print(math.exp(x))  # in this following code the math library returns the value of the variable raise to '^' e ,
print()

# i.e it returns the value of x^e
#  Now the value of e is
print(math.e)

print()

#  Also we can se it to get the values of common math functions such as pi
print(math.pi)

print()

# You can slo get the square root of numbers by using the keyword sqrt
print(math.sqrt(9))
print(math.sqrt(25))

# Lists (detailed)
# List is  a collection of data. It can hold values with multiple data types
#  We have created basic lists above so i won't be repeating it

# Let's create a nested list
list1 = [[0, 1, 2], ['a', 'b', 'c']]
print(list1)

print()

print(list1[-1])  # To get the 1st term from behind

print()

# Operations on a list
z = [100]
print(z * 100)

print()

# Let's concatenate lists
A = ['Amaan ']
H = ['Hasw']
H1 = ['are']
conc = A + H + H1
print(conc)

# Methods in lists
num = [1, 2, 3, 4]
print(num)
num.append(5)
print(num)
num.extend(A)  # it is used to add lists in lists
print(num)
num.insert(6, 'Hasware')  # To insert the values in between of a list
print(num)
num.remove('Hasware')
print(num)

print()

# To sort out the list in alphabetical order we use the keyword Sort
abc = ['d', 'c', 'b', 'a']
print(abc)
abc.sort()
print(abc)

print()

#  Tuples (In Detail)
#  Arrays can have only 1 type of data type in them but tuples & lists can have multiple data types. Also Tuples are
#  immutable meaning their values cannot be changed
#  They are used by '( )'
emp = ()
print(emp)
print(type(emp))
#  note tuples can be empty
#  Tuples may or may not use paranthesis but if not using paranthesis they must end with a comma
emp = "Empty",
print(emp)
print(type(emp))
# You can access the elements of tuple the same you did for lists

print()

# Concatenation
num1 = (1, 2, 3, 4)
city = ('Pune', 'Mumbai' , 'Chennai')
ciNum = num1+city
print(ciNum)
print(type(ciNum))

print()

# You can also nest tuples the way you did for lists
nest = (city, num1)
print(nest)

#  Again the basic methods are slicing, unpacking, deleting

print()

# Strings
# To use quotation marks in side  your string , you can use the help of backslash key,For Eg:
str = "Tim's Birthday"
str1 = "Tim said \"I'm busy\" "
print(str1)
