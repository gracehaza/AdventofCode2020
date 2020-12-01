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
            for k in range (1,len(lineslist)):
                numberstring3=lineslist[k]
                number3 = float(numberstring3)
                if number+number2+number3 == 2020:
                    print'Product: ',number*number2*number3
                    break
                else:
                    continue # executed if inner loop (over k) did not break
                break # executed if inner loop (over k) did break

            else:
                continue #executed if inner loop (over j) did not break
            break
    
        else:
            continue  # executed if inner loop (over i) did not break
        break
