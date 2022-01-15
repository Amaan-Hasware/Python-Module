# If-Else Statements
# if (condition) :
#   Statements to execute if condition is true
# else:
#   Statements to execute if condition is false
# Example:
a = 20
if (a > 50):
    print(str(a) + " is greater than 50")
else:
    print(str(a) + " is smaller than 50")

# Nested If Else statements
c = 52
if c < 25:
    print("c is smaller than 25")
    if c % 2 == 0:
        print("c is smaller than 25 and is an even number")
    else:
        print("c is smaller than 25 and an odd number ")
elif c % 2 == 0:  # Note : Elif means Else : if (), meaning in else block a new if statement is introduced
    print("c is greater than 25 and even number")
else:
    print("c is greater than 25 and an odd number")
