# Working Of Threads
# Let's write a program for printing out a number followed out by a Double and square of the number
import time
from threading import *
import time


class Demo:
    def num(self):
        for i in range(0, 6):
            print("The Number is ", i)
        print()
    def double(self):
        for i in range(0, 6):
            print("The double of number is ", i * 2)
        print()

    def square(self):
        for i in range(0, 6):
            print("The square of number is ", i * i)
        print()


obj = Demo()

t1 = Thread(target=obj.num)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)


# But the code will sometimes or many times end without the proper execution of the code, that's why we use the join
# function we make sure that the program will not end without the full execution of all the threads
t1.join()
t2.join()
t3.join()


print("This is the main thread")

