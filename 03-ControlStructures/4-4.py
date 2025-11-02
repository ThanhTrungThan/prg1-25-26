###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = str(input("enter your university's name: "))
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(f'original university name: {university}') # original university name
print(f'expanded university name: {university_expanded}') # expanded university name