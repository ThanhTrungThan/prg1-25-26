###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
import math
number1 = float(input('enter the first number: '))
number2 = float(input('enter the second number: '))
operator = str(input('enter operator (+,-,*,/): '))

if operator == '+' :
    result = number1 + number2
elif operator == '-' :
    result = number1 - number2
elif operator == '*' :
    result = number1 * number2
elif operator == '/' :
    result = number1 / number2

# print result
print(f'{number1} {operator} {number2} = {result}')