###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = float(input('enter side a: '))
b = float(input('enter side b: '))
c = float(input('enter side c: '))
s = 0.5*(a+b+c)

def triangle_area(a,b,c):
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result

print((triangle_area(a,b,c)))