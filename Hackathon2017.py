# -*- coding: utf-8 -*-
"""
Programer Name: Colin Orian
Program Description: Gets the distance values between three constant points
 from a dataset. These distances will be used for trialteration. 
"""
#Keep an eye out for the NMS_SCALE_CORRECTION = 4.0 distance = distance / 4.0

inFile = open("HMSLegacyData.txt")
inLines = inFile.readlines()

distances = list()
points = list()
for line in inLines:
    value = line[1:14]
    if(value == "DistanceValue"):
        new_line = line.split("|")
        entries = list()
        entries.append(new_line[3])
        entries.append(new_line[5])
        entries.append(new_line[7])
        entries.append(new_line[9].strip())
        distances.append(entries)

"""
TODO: Trilaterate the points to find x,y,z values. 
"""


        
