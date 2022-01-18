# Threading
# A Process:
#           A Process is an executable instance of a computer program
# A Thread exists within a Process

# A Thread:
#           A Thread is a sequence of instructions in a program that can be executed independently  of the remaining
#           program
#
# How to use:
# 1) from threading Import *
# 2) create a method which will run on a child thread and the other part on a main thread

from threading import *

# Let's create an example to show the working of Thread

# 1st Way of using threads

# def show():  # A method is created
#     print("This is child thread")
#
#
# t = Thread(target=show())
# t.start()
#
# print("This is parent thread")

# print()


# 2nd Way of using threads
# In this child thread t is running on1 thread and the for loop below it is running on the main thread simultaneously,
# Hence the output will be a mix-matched of both the codes (It is context Switching, we do not know the order of the
# output)


# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("\nThis is child class")
#
#
# t = MyThread()
# t.start()
#
# for i in range(5):
#     print("\nThis is main thread")


# 3rd Way of using threads
# In this child thread t is calling out the target obj and as obj=Demo class, the class demo is running on 1  thread
# and the for loop below it is running on the main thread after the object obj is done running,
# Hence the output will give the output of both the codes one after the another and not simultaneously

# class Demo:
#     def show(self):
#         for i in range(5):
#             print("This is the child thread")
#
#
# obj = Demo()
# t = Thread(target=obj.show())
# t.start()
#
# for i in range(5):
#     print("This is the parent thread")

# Context Switching:
#                   Storing the state of a Process/Thread and resuming its execution at a later time is called
#                   Context Switching (We saw this in the 2nd way above)

# Multithreading:
#               A model where the multiple threads within a process execute independently while sharing the same
#               resources is called multithreading

