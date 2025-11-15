def f(amount_to_pay):
    c5 = amount_to_pay // 5      #take the quotient
    remain = amount_to_pay % 5    #take the remain

    c2 = remain // 2
    c1 = remain % 2

    return c1 + c2 + c5

if __name__ == "__main__":
    print(f(23))  # returns 6       
    print(f(8))   # returns 3