#Eysteinn Örn Jónsson
#HR 20/8/19
'''
#partur 1
m_str = input('Input m: ')  # do not change this line
m_float = float(m_str)# change m_str to a float
c_int = 300000000# remember you need c
e = (m_float * pow(c_int,2)) # e = 
print("e =", e)  # do not change this line
'''
'''
#partur 2
in_str = input("Input s: ")
in_int = int(in_str)# in_int =
print("in_int = ", in_int)
in_float = float(in_str)# in_float =
print("in_float = ", in_float)
'''
'''
#partur 3
import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints
x1_int =int(x1_str)
y1_int =int(y1_str)
x2_int =int(x2_str)
y2_int =int(y2_str)
d = math.hypot(abs(x1_int - x2_int),abs(y1_int - y2_int))#  d =
print("d =",d)  # do not change this line
'''
'''
#partur 4
weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line
weight_float = float (weight_str)
height_m_float = float(height_str)/100
bmi = weight_float/((pow(height_m_float,2)))
print("BMI is: ", bmi) # do not change this line
'''
'''
#partur 5
x_str = input("Input x: ")
x_int = int (x_str)# remember to convert to an int
first_three = x_int // 1000# first_three =
last_two = x_int % 100# last_two =
middle_two = (x_int)//100%100# middle_two =
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)
'''
'''
#partur 6
secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = secs_int//3600# hours =
minutes = (secs_int%3600)//60# minutes =
seconds = (secs_int%60)//1# seconds =
print(hours,":",minutes,":",seconds) # do not change this line
''
