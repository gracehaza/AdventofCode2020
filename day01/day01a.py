import math

filepath = 'day01input.txt'

with open(filepath,"r") as filenow:
    lineslist = filenow.readlines()
    for i in range(0,len(lineslist)):
        numberstring=lineslist[i]
        number = float(numberstring)
        sum = 0
        for j in range (1,len(lineslist)):
            numberstring2 = lineslist[j]
            number2 = float(numberstring2)
            if number+number2 == 2020:
                print'Product: ',number*number2
                break
        else:
            continue # executed if inner loop did not break
        break # executed if inner loop did break
