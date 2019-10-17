# FE520 - Homework 3
# Author: Yoohan Ko
# "I pledge my honor I have abided by the Stevens Honor System"

# import the generator and point classes from Python modules
import time
from generator import *
from point import *

start_time = time.time()

# ==============================================================================================================
print("Using LCG generator:")

# 1) Populate 10,000,000 random points within this square
myLCG = LCG(1, 1103515245, 12345, 4294967296)

# generate 20,000,000 random numbers
LCG_num = myLCG.getSequence(20000000)
# print(LCG_num)

LCG_num_adjusted = []
# convert from a range of 0 to 1 to -1 to 1
for i in range(len(LCG_num)):
    new_val = (LCG_num[i] * 2) + -1
    LCG_num_adjusted.append(new_val)

# print(LCG_num_adjusted)

#splitting LCG_num_adjusted into two half sublists
n = len(LCG_num_adjusted)/2
print("The total number of points generated is: " + str(int(n)))
LCG_num_split1 = LCG_num_adjusted[:int(n)]
LCG_num_split2 = LCG_num_adjusted[int(n):]

# print(LCG_num_split1)
# print(LCG_num_split2)

# creating the points
points = []
for i in range(int(n)):
    temppoint = Point(LCG_num_split1[i], LCG_num_split2[i])
    points.append(temppoint)

# determine whether points are within the circle
inside_circle = 0
for i in range(int(n)):
    if points[i].distance() < 1:
        inside_circle += 1

print("The number of points inside the circle is: " + str(inside_circle))

# Give the estimate of the above ratio, and the difference between yours and the theoretical one
ratio = inside_circle / n
print("The ratio of the points inside of the circle to those outside is: " + str(ratio))
difference = abs(ratio - 0.78539816339)
print("There is a difference of: " + str(difference) + "\n")

# ==============================================================================================================
print("Using SCG generator:")
mySCG = SCG(2, 1103515245, 12345, 4294967296)
# generate 20,000,000 random numbers
SCG_num = mySCG.getSequence(20000000)
# print(LCG_num)

SCG_num_adjusted = []
# convert from a range of 0 to 1 to -1 to 1
for i in range(len(SCG_num)):
    new_val = (SCG_num[i] * 2) + -1
    SCG_num_adjusted.append(new_val)

# print(SCG_num_adjusted)

#splitting SCG num_adjusted into two half sublists
n = len(SCG_num_adjusted)/2
print("The total number of points generated is: " + str(int(n)))
SCG_num_split1 = SCG_num_adjusted[:int(n)]
SCG_num_split2 = SCG_num_adjusted[int(n):]

# print(SCG_num_split1)
# print(SCG_num_split2)

# creating the points
points2 = []
for i in range(int(n)):
    temppoint = Point(SCG_num_split1[i], SCG_num_split2[i])
    points2.append(temppoint)

# determine whether points are within the circle
inside_circle = 0
for i in range(int(n)):
    if points2[i].distance() < 1:
        inside_circle += 1

print("The number of points inside the circle is: " + str(inside_circle))

# Give the estimate of the above ratio, and the difference between yours and the theoretical one
ratio = inside_circle / n
print("The ratio of the points inside of the circle to those outside is: " + str(ratio))
difference = abs(ratio - 0.78539816339)
print("There is a difference of: " + str(difference) + "\n")

# record the time consumed by your program by using the time package
print("The program took %s seconds to run" % (time.time() - start_time))