def f(num,even):
    num_str = str(num)
    total = 0

    for char in num_str:
        d = int(char)
        if even:
            if d % 2 == 0:
                total += d
        else:
            if d %2 != 0:
                total += d
    return total

if __name__ == "__main__":       
    print(f(3124,False)) #returns 4
    print(f(3124,True)) #returns 6