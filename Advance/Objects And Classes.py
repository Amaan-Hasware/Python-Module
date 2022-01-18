# Objects And Classes
# Every instance in python is an object
# And Everything in Python is an object of some class
# That's why you get the "class <str>" "class <int>" "class <float>" because it means that the variable holding it is
# an object having class "class <str>" or  "class <int>" or "class <float>"
# A class is a blueprint for similar objects
#
# Example: A Person
# A Person has respective features/attributes which are name,age,gender and some behaviour that is talk and vote
#
# Same is the case with objects and classes
# A person is a class having different objects obj1 and obj2 and ca have different features such as name,age,gender and
# functions such as talk and greet

# A class is created using the keyword class
class Person:
    def __init__(self, name, gender, age):  # The reference object here is self
        # self.name = "Amaan"
        # self.gender = "Male"
        # self.age = 18
        self.name = name
        self.gender = gender
        self.age = age

    #   Here you defined the attributes of an object of the class person, now let's define the functions(Behaviour of
    #   that object
    # Note A function tied and called via an object are called methods
    def talk(self):
        print("Hi, I am " + self.name)

    def vote(self):
        if self.age < 18:
            print("I am not eligible to vote")
        else:
            print("I am  eligible to vote")

# The below commented out code is for the method __init__  in which no parameters of taking an input is mentioned
# obj = Person()
# Person.talk(obj)
# Person.vote(obj)
#
# print()  # For new extra line
# #       OR
#
# obj.talk()
# obj.vote()

# Now let's create 2 objects as obj1 and obj2 of the type Person (which is our class)
# Everytime our object is created, our __init__ method is called.
# If our object needs to have separate values , we need to give the parameters in our __init__ method


obj1 = Person("Rabia", "Female", 16)
obj2 = Person("Amaan", "Male", 18)

obj1.talk()
obj1.vote()
obj2.talk()
obj2.vote()

print(obj1.name)
print(obj2.name)