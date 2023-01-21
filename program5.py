#radius is 30 meters

#Area of circle pi*radius^2
import math
radius = 30
_area_of_circle_= math.pi*radius**2
print("Area of Circle = ",_area_of_circle_)

#Circumference of Circle is 2*pi*radius
_circum_of_circle_ = math.pi*2*radius
print("Circumference of Circle = ",_circum_of_circle_)

#Taking radius as user input
radius_inp = int(input("enter the radius = "))
_area_of_circle_= math.pi*radius_inp**2
print("Area of Circle = ",_area_of_circle_)

