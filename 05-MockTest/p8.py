def f(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))
