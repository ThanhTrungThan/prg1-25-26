def f(binary_number):
    for digit in binary_number:
        if digit not in '01':
            return False
    return True

if __name__ == "__main__":       
    print(f("101101")) #returns True
    print(f("1311a10100")) #returns False