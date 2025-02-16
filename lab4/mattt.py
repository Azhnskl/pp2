#task1
'''
import math
value = int(input("Enter  degree: "))

converted_value = (value * math.pi)/180

print(f"Radians: {converted_value:.6f}")
'''
#task2
'''
height = int(input ("Enter height: "))
base1 = int(input ("Enter 1 base: "))
base2 = int(input ("Enter 2 base: "))

area = ((base1+base2)/2)*height
print(f"Area_Of_Trapezoid: {area}")
'''
#task3
'''
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

if n == 4:  
    area = s ** 2
else:
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area}")
'''
#task4
'''
base = float(input ("Enter base: "))
length = float(input ("Enter length of side: "))
area = base * length
print (f"Area of the parrallelogram: {area}")
'''