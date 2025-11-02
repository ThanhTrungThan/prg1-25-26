###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0

for i in range(int(input('enter starting number: ')), int(input('enter ending number: '))):
    sum += i

print(f'Sum is {sum}')