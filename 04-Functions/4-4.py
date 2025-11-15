def s(x):
    x = abs(x)
    strx = str(x)
    d = 0

    for i in strx:
        d += int(i)
    return d

any = int(input("enter any number: "))
res = s(any)
print(res)