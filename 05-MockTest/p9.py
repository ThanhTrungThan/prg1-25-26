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
    