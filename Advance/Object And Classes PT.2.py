class car:
    def __init__(self, year, speed):  # Here when an object is defined with the type car (Our class), it will take 2
        # arguments for year and speed (FTP)
        self.year = year
        self.speed = speed

    def getYear(self):
        print('Release of model was in the year: ', self.year)  # Here (FTP) will use this function to print the
        # Release date of the car he(FTP) has used while creating under the type car and the respective argument which
        # was given

    def getSpeed(self):
        print('Maximum speed is: ', self.speed)  # Here (FTP) will use this function to print the Max speed of the
        # car he has used while creating under the type car and the respective argument which was given

    def setYear(self, year):  # here the year value will be set via the programmer
        self.year = year

    def setSpeed(self, speed):  # here the speed value will be set via the programmer
        self.speed = speed


BMW = car(2020, 190)
FORD = car(2017, 178)

print(type(BMW))

car.getSpeed(BMW)
car.getSpeed(FORD)

car.getYear(BMW)
car.getYear(FORD)

print()

print("Till here the info was given via classes, let's try the set method")

print()

BMW.setSpeed(200)
FORD.setSpeed(185)

BMW.setYear(2022)
FORD.setYear(2021)

car.getSpeed(BMW)
car.getSpeed(FORD)

car.getYear(BMW)
car.getYear(FORD)

print()

print("INHERITANCE")

print()


# Inheritance: It  is a mechanism for a new class to use the features of another class
class bike(car):  # Bike is now a child class to the class car
    def accelerate(self):
        print('137')


class SUV(car):  # SUV is now also a child class to the class car
    def accelerate(self):
        print('168')


ducati = bike(2017, 205)
ducati.getSpeed()
ducati.getYear()
ducati.accelerate()

hummer = SUV(1, 1)
hummer.setSpeed(165)
hummer.setYear(2014)
hummer.getSpeed()
hummer.getYear()
hummer.accelerate()

# Encapsulation: The feature of preventing data from direct access is called Encapsulation
# The above code of creating child class bike and SUV from the parent class car is the example of it:
# You can make changes in the child classes as much as yiu want and add new methods in it but not change the parent
# class

# Polymorphism: polymorphism is the feature of using the same function in different/multiple ways
# Example is using the accelerate function in different ways  (Assigning different values in SUV and bike)
