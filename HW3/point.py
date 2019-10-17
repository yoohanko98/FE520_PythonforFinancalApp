# FE520 - Homework 3
# Author: Yoohan Ko
# "I pledge my honor I have abided by the Stevens Honor System"

import math

# class to represent the points in a rectangular coordinate
class Point:
    # class should have data attributes that store its x coordinate and y coordinate
    def __init__(self, xpoint, ypoint):
        self.xpoint = xpoint
        self.ypoint = ypoint

    # function attribute distance to calculate its distance from the origin point
    def distance(self):
        # using the mathematical formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        self.distance_value = math.sqrt(self.xpoint**2 + self.ypoint**2)
        return self.distance_value


# print("creating a test point")
# testPoint = Point(0.3, 0.7)
# print(testPoint.distance())