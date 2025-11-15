def f(card_number):
    first2 = card_number[0:2] #first 2 character is visibale
    last4 = card_number[12:16] #last 4 character is visibale
    middle = len(card_number) - 6 #length of card_number (a number) minus 6 (first 2 and last 4)
    star = '' #set '*'

    for number in range(middle):
        star += '*'
    #middle characters are visibaled as '*' 
    return first2 + star + last4 


if __name__ == "__main__":
    print(f('5290312400019022')) # returns "52**********9022"