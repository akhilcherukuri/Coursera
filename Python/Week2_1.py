import math,random

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

def future_value(present_value,annual_rate,years):
    return present_value * (1+ annual_rate * 0.01) ** years

def name_tag(first_name,last_name):
    return "My name is " + first_name + " " + last_name + "."

def name_and_age(name,age):
    return name + " is " + age + " years old."

def point_distance(x_0,y_0,x_1,y_1):
    return ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5

def triangle_area(x_0,y_0,x_1,y_1,x_2,y_2):
    # Heron's Formula + Distance Formula
    a = ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5 
    b = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
    c = ((x_2 - x_0) ** 2 + (y_2 - y_0) ** 2) ** 0.5
    s = (a + b + c)/2
    return math.sqrt( s * (s-a) * (s-b) * (s-c))
    
def print_digits(number):
    tens_place = number // 10
    ones_place = number % 10
    return "The tens digit is " + str(tens_place) + " and the ones digit is " + str(ones_place) + "." 

def powerball():
    integer1 = (random.randrange(1, 60))
    integer2 = (random.randrange(1, 60))
    integer3 = (random.randrange(1, 60))
    integer4 = (random.randrange(1, 60))
    integer5 = (random.randrange(1, 36))
    return integer1,integer2,integer3,integer4,"powerball : " + str(integer5)



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

present_value,annual_rate,years = 1000, 7, 10	
print("future_value : $" + str(future_value(present_value,annual_rate,years)))

first_name,last_name = "Akhil","Cherukuri"
print(name_tag(first_name,last_name))

name,age = "Akhil Cherukuri","23"
print(name_and_age(name,age))

x_0,y_0,x_1,y_1 = 2,2,5,6
print("point_distance : " + str(point_distance(x_0,y_0,x_1,y_1)))

x_0,y_0,x_1,y_1,x_2,y_2 = -2,4,1,6,2,1 
print("triangle_area : " + str(triangle_area(x_0,y_0,x_1,y_1,x_2,y_2)))

number = 58
print("print_digits : " + str(print_digits(number)))

print(powerball())