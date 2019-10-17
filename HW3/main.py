# FE520 - Homework 3
# Author: Yoohan Ko
# "I pledge my honor I have abided by the Stevens Honor System"

import numpy as np

### Part I: Class practice (30 pts)
class Rectangular:

    # constructor should assign the two attributes
    def __init__(self, length, width):
        # Two data attributes: length & width using instance variables
        self.length = length
        self.width = width

    # function for area()
    def area(self):
        return self.length * self.width

    # function for perimeter()
    def perimeter(self):
        return 2 * self.length + 2 * self.width

# inherited class Square from Rectangular
class Square(Rectangular):
    def __init__(self, length):
        super().__init__(length, length)


# creating an instance of Rectangular class called myRec
myRec = Rectangular(10,20)

# print statements to make sure the function is working correctly
print("The area of the rectangle is: " + str(myRec.area()))
print("The perimeter of the rectangle is: " + str(myRec.perimeter()) + "\n")

# creating an instance of Square class called mySq
mySq = Square(30)

# print statements to make sure the Square class has inherited the functions correctly
print("The area of the square is: " + str(mySq.area()))
print("The perimeter of the square is: " + str(mySq.perimeter()))

# define two numpy array with a size of 10 named length and width
length = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], dtype = np.int32)
width = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50], dtype = np.int32)

# test Rectangular class with np array as the input
for i in range(10):
    print("Inputting Length = " + str(length[i]) + " and Width = " + str(width[i]))
    tempRec = Rectangular(length[i], width[i])
    print("The area of the rectangle is: " + str(tempRec.area()))
    print("The perimeter of the rectangle is: " + str(tempRec.perimeter()) + "\n")


### Part II: Display Time (20 pts)

# create a Time class and initialize it with hours, minutes, and seconds
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # method addTime should take the additional time and add it to the current time variables
    def addTime(self, add_h, add_m, add_s):
        # first, add the seconds
        self.seconds += add_s
        if self.seconds > 59:
            self.seconds -= 60
            self.minutes += 1

        # second, add the minutes
        self.minutes += add_m
        if self.minutes > 59:
            self.minutes -= 60
            self.hours += 1

        # lastly, add the hours
        self.hours += add_h

    # method displayTime should print the time
    def displayTime(self):
        print("The current time values are: " +
              str(self.hours) + " Hours, " +
              str(self.minutes) + " Minutes, " +
              str(self.seconds) + " Seconds.")

    # method displaySeconds should display the total seconds in the time
    def displaySeconds(self):
        total_time = self.hours * 3600 + self.minutes * 60 + self.seconds
        return total_time

myTime = Time(5, 15, 35)
myTime.displayTime()
myTime.addTime(2, 55, 50)
myTime.displayTime()
print("The total number of seconds are: " + str(myTime.displaySeconds()))