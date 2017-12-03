# -*- coding: utf-8 -*-
"""
Programer Name: Colin Orian
Program Description: Stores points on an x,y,z plane based on having the same
slope
"""

#Use numpi to solve system of equation
import random
import numpy as np
points = list()

"""
Calcualtes the equation of a plane using three points.
Retreaved from:
http://kitchingroup.cheme.cmu.edu/blog/2015/01/18/
Equation-of-a-plane-through-three-points/
"""
def planeCalc(point1, point2, point3):
    
    point1 = np.array(point1)
    point2 = np.array(point2)
    point3 = np.array(point3)
    
    vect1 = point3 - point1
    vect2 = point2 - point1
    
    crossProd = np.cross(vect1, vect2)
    print(crossProd)
    if(len(crossProd) != 3):
        return
    a, b, c = crossProd
    
    d = np.dot(crossProd, point3)
    
    print("The equation is {0}x + {1}y + {2}z = {3}".format(a,b,c,d))
    

#Creates 20 points with random x,y,z values
for i in range(20):
    coOrds = list() #Co-ords 1 = x, 2 = y, 3 = z
    for j in range(3):
        coOrds.append(random.randint(-100, 100))
    points.append(coOrds)

#Defines Dictnaries and keys
yOverX = {}
yOvXKeys = list()

yOverZ = {}
yOvZKeys = list()

zOverX = {}
zOvXKeys = list()
"""
Iterates over the points and stores the points with the same slope into the 
dictonary using the slope as a key
"""
for i in range(len(points)):
    
    # Slope = y / x
    temp = list()
    if(points[i][0] != 0):
        slope = points[i][1] / points[i][0]
        if(slope in yOverX):
            temp = yOverX[slope]
        else:
            yOvXKeys.append(slope)
        temp.append(points[i])
        yOverX[slope] = temp
        
    # Slope = y / z
    temp = list()
    if(points[i][2] != 0):
        slope = points[i][1] / points[i][2]
        if(slope in yOverZ):
            temp = yOverZ[slope]
        else:
            yOvZKeys.append(slope)
        temp.append(points[i])
        yOverZ[slope] = temp
    
    # Slope = z / x
    temp = list()
    if(points[i][0] != 0):
        slope = points[i][2] / points[i][0]
        if(slope in zOverX):
            temp = zOverX[slope]
        else:
            zOvXKeys.append(slope)
        temp.append(points[i])
        zOverX[slope] = temp
"""
TODO: Give a margin of error for the slopes (ex. 1.001 will be hashed into
1.000)
Check how many points are in the same hash and if it reaches a threashold, 
display the plane's equation and display the plane.
"""

