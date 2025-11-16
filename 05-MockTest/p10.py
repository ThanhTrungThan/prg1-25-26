def f(sentence):
    ascii_sum = 0 
    for char in sentence:
        ascii_sum += ord(char)
    if ascii_sum % 3 == 0:
        return True
    else: 
        return False
    

if __name__ == "__main__":
    print(f("university"))
    print(f("hello world"))
    print(f("student"))
    