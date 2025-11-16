def f(n):
    # special condition: first 2 number
    if n == 1:
        return 0
    if n == 2:
        return 1

    # start with first 2 number
    prev = 0   # F1
    curr = 1   # F2

    pos = 3  # begin with f3

    # loop to fn
    while pos <= n:
        new = prev + curr

        # fn = f(n-1) + f(n-2)
        prev = curr
        curr = new

        pos += 1

    # curr is fn
    return curr

if __name__ == "__main__":
    print(f(5))
    print(f(9))