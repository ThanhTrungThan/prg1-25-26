def f(amount_to_pay):
    c5 = amount_to_pay // 5
    remain = amount_to_pay% 5

    c2 = remain // 2
    c1 = remain % 2

    sum = c5 + c2 + c1
    return sum

if __name__ == "__main__":
    print(f(8))