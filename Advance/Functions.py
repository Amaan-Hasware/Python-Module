# Functions
#  A Function is a set of code that performs some task
# Syntax:
#       def function_name(parameters if needed from user):
#       statements
def welcome():
    print("Good Morning")


# A function need to be called
welcome()


#  Creating a function that will take 2 numbers from user and return their addition

def AddFromUser():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    sum = (num1 + num2)
    return sum


def add(num1=0, num2=0):  # Here =0 means the default value will be set to 0 if user do not give
    sum = (num1 + num2)
    return sum

def unknown(*a):
    total = 0
    for i in a:
        total = total + i
    print(total)

# Note:
# Python does not support function overloading. When we define multiple functions with the same name,
# the later one always overrides the prior and thus, in the namespace
# Hence, we created 2 functions in which 1 takes the input from the programmer (add function) and the other from the
# user (AddFromUser function


x = add(4, 5)  # Took from programmer
print(x)

x = AddFromUser()  # Took from user
print(x)


#  Now if user doesn't know how many inputs are to be given then we use the parameters as list

x = unknown(4, 5, 6, 5)
print(x)