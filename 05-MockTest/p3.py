def f(name):
    words = name.split() #take word by word
    acronmy = ''  #set a acronym
    for word in words: 
        acronmy += word[0] #acronym -> first letter of word
    return acronmy
print(f("Internet of Things"))        #return 'IoT'
print(f("For Your Information"))      #return 'FYI'
print(f("Python"))                    #return 'P'
