import math

filepath = 'day02input.txt'

with open(filepath,"r") as filenow:
    lineslist = filenow.readlines()
    validpasswordcount = 0
    for i in range(0,len(lineslist)):
        line=lineslist[i]
        line.replace('-',' ')
        numbers=[int(s) for s in line.replace('-',' ').split() if s.isdigit()]
        first = numbers[0]
        second = numbers[1]
        lettersonly=""
        specialletter=""
        for character in line:
            if character.isalpha():
                lettersonly += character
        specialletter=lettersonly[0]
        if lettersonly[first] == specialletter and lettersonly[second] !=specialletter:
            validpasswordcount += 1
        elif lettersonly[first] !=specialletter and lettersonly[second] == specialletter:
            validpasswordcount += 1
        
    print 'Valid password count: ',validpasswordcount
