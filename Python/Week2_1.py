import math

def miles_to_feet(miles):
    feet = miles * 5280
    return feet

def total_seconds(hours,minutes,seconds):
    hours_to_secs = hours * 60 * 60
    minutes_to_secs = minutes * 60
    return (hours_to_secs + minutes_to_secs + seconds)
    
def rectangle_perimeter(width,height):
    return (width+height)*2

def rectangle_area(width,height):
    return (width * height)

def circle_circumference(radius):
    return 2 * math.pi * radius

def circle_area(radius):
    return math.pi * radius ** 2

miles = 2
print("miles_to_feet : " + str(miles_to_feet(miles)))    

hours,minutes,seconds = 7,21,37
print("total_seconds : " + str(total_seconds(hours,minutes,seconds)))

width,height = 2,3
print("rectangle_perimeter : " + str(rectangle_perimeter(width,height)))

width,height = 4,7
print("rectangle_area : " + str(rectangle_area(width,height)))

radius = 8
print("circle_circumference : " + str(circle_circumference(radius)))

radius = 8
print("circle_area : " + str(circle_area(radius)))