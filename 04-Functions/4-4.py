def digits_sum(number):
    number = abs(number)
    number_str = str(number)
    sum_digits = 0

    for digits_char in number_str:
        sum_digits += int(digits_char)
    return sum_digits


any_number = int(input('enter any number: '))
result = digits_sum(any_number)
print(result)