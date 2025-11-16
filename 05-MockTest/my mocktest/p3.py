def f(text):
    vowels = 'aeiyou'
    result= ""
    for i in text:
        if i not in vowels:
            result += i
    return result


if __name__ == "__main__":
    print(f("programming"))