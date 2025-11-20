"""
#p3 Initials - acronmy
def f(full_name):
    full_name = full_name.split()
    initials = []
    
    for word in full_name:
        if word:
            initial = word[0].upper()
            initials.append(initial)
    return ". ".join(initials) + "."

if __name__ == "__main__":
    print(f("Than Thanh Trung"))


#p4 Masking
def f(phone_number):
    first3 = phone_number[0:3]
    last2 = phone_number[-2:]
    middle = len(phone_number) - 5
    star = ''

    for i in range(middle):
        star += '*'
    return first3 + star + last2
if __name__ == "__main__":
    print(f('501987654'))



#p5 Hexadecimal Check
def f(hex_number):
    valid_char = '123456789abcdefABCDEF'

    for char in hex_number:
        if char not in valid_char:
            return False
    return True
if __name__ == "__main__":
    print(f('10G'))


#p6 Sum of Digits by Parity
def f(number,odd):
    total = 0
    number = str(number)

    for char in number:
        d = int(char)

        if odd:
            if d % 2 != 0:
                total += d
        else:
            if d % 2 == 0:
                total += d
    return total
if __name__ == "__main__":
    print(f(3124, False))




#p7 Factorial
def f(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    
    total = 1
    for i in range(1, 1+n):
        total *= i
    return total
if __name__ == "__main__":
    print(f(5)) 

""" 

#p9 
def f(sentence):
    vowels = 'aeoiuy'
    count = 0
    for i in sentence.lower():
        if i in vowels:
            count += 1
    return count
    

if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))
