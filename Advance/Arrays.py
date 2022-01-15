# Arrays hold multiple value of same type
from array import *

# syntax:
#       var_name = array (type code [elements])
#                           typecode is written below also the img is attached in the folder

arr = array('i', [1, 2, 3, 4, 5])  # i stands for integers
print(arr)

print(arr.buffer_info())  # This gives info about the location of the array on our device along with it's location

# Accessing arrays is also done via index numbers starting form 0
print(arr[2])

print()

# For loops can also be used on Arrays
for i in arr:
    print(i)
#  the main difference between accessing an array via loops and print method is that in print it also gives the
#  useless info such as 'array' 'i' then the square brackets etc etc

print()

# To get the pointers(index numbers) along side with the values we use
for pnt in range(5):
    print(pnt, arr[pnt])

print()

# We can also reverse an Array
arr.reverse()
print(arr)

print()

#  It also has append attribute
arr.append(36)
print(arr)

print()

# Same for the remove function
arr.remove(36)
print(arr)

print()

arr.reverse()
print(arr)
print()
# To get the element at a particular index number we use,
print(arr[3])
# And To get the index number of a particular element we use,
print(arr.index(4))

# Let's create an array by taking the inputs from the user
usr = array("i", [])
s = int(input("Size of your array: "))
print("Enter %d elements" % s)
for i in range(s):
    x = (int(input()))
    usr.append(x)
print(usr)