import math

filepath = 'day02input.txt'

with open(filepath,"r") as filenow:
    lineslist = filenow.readlines()
    validpasswordcount = 0
    for i in range(0,len(lineslist)):
        line=lineslist[i]
        line.replace('-',' ')
        numbers=[int(s) for s in line.replace('-',' ').split() if s.isdigit()]
        min = numbers[0]
        max = numbers[1]
        lettersonly=""
        specialletter=""
        for character in line:
            if character.isalpha():
                lettersonly += character
        specialletter=lettersonly[0]
        lettercounter=0
        for i in range (1,len(lettersonly)):
            if lettersonly[i] == specialletter:
                lettercounter += 1
        if lettercounter >= min and lettercounter <= max:
            validpasswordcount += 1
        
    print 'Valid password count: ',validpasswordcount
