import math

class Point:

    def __init__(self,parameter1,parameters2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

class LineSegment:

    def __init__(self,segmentStart: Point,segmentEnd: Point):
        self.segmentStart = segmentStart
        self.segmentEnd = segmentEnd

    def slope(self):
        result = (self.segmentStart.parameter1 - self.segmentEnd.parameter1) / (self.segmentStart.parameter2 - self.segmentEnd.parameter2)
        return result

    def length(self):
        distance = math.sqrt( pow((self.segmentStart.parameter1 - self.segmentEnd.parameter1),2) + pow((self.segmentStart.parameter2 - self.segmentEnd.parameter2),2 ))
        return distance
