# Loops in Python
# There are 2 types of Loops: For, While


# For Loops
# It is used to iterate over a sequence which could be a list,array,tuple or a string
# Syntax:
#       for counter in sequence:
#            statements
# Demo
x = [1, 4.2, "Ammo-Nation"]
# You can print every element of a loop either via index number or by For loop
for i in x:
    print(i)

# To print every character of a string separately
str = 'Amaan Hasware'
for i in str:
    # print(i)  # This will print each character on new line
    print(i, end="")  # end='' is for not using next line to print, but the same line

print()

# Now comes the part of where you are introduced to Range() Function, range function automatically sets the range for
# you in the loop,
#  For example:
for i in range(1, 11):
    print(i, end=' ')

for i in range(0, 11, 2):  # Here we have added 2 at the end to get the elements after 2-2 gap of each (even numbers)
    print(i, end=' ')

print()

# To get the sum of the even numbers upto 20
sum = 0
for i in range(0, 21):
    if i % 2 == 0:
        sum = sum + i
print(sum)

#  To print a Right  Triangle pattern
n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Factorial Example using for loop
num = int(input('Number: '))
factorial = 1
if num < 0:
    print("Number should be positive")
elif num == 0 or num == 1:
    print("Factorial is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)


print()

    # While loop
    # It is used in a sequence in which we are unaware about the number of iterations that is to be performed

# Writing a code that will give u sum of even numbers
i = 1
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)




# A game of guessing the mnumbers
import random

n = 20
to_be_guessed = int(n * random.random())
guess = 0
while guess != to_be_guessed:
    guess = int(input("Enter your number: "))
    if guess > to_be_guessed:
        print("Number too large")
        print()
    elif guess < to_be_guessed:
        print("Number to small")
        print()
print("Congo, you won! ")
