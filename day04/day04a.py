
filepath = 'day04input.txt'

def look_at_passport(begin,end):
    with open(filepath,"r") as filenow:
        lineslist=filenow.readlines()
        requirements=['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
        validity=[]
        for k in range(0, len(requirements)):
            valid = False
            for j in range(begin,end):
                line=lineslist[j]
                bool = line.find(requirements[k])
                if bool != -1:
                    valid = True
            validity.append(valid)
        return validity
        
def main():
    with open(filepath,"r") as filenow:
        totalpassportcount = 0
        invalidpassportcount = 0
        lineslist = filenow.readlines()
        min = 0
        for i in range(0,len(lineslist)):
            line = lineslist[i]
            if line =="\n":
                max = i
                validityarray = look_at_passport(min, max)
                totalpassportcount +=1
                for l in range(0,len(validityarray)):
                    if validityarray[l] == False:
                        invalidpassportcount += 1
                        break  #prevents double counting
                min = i

            if i == len(lineslist)-1:
                lastvalidityarray = look_at_passport(max, len(lineslist))
                totalpassportcount +=1
                for m in range (0,len(lastvalidityarray)):
                    if lastvalidityarray[m] == False:
                        invalidpassportcount += 1
                        break #prevents double counting

    validpassportnumber = totalpassportcount - invalidpassportcount
    print 'total valid passport: ', validpassportnumber


if __name__ == "__main__":
    main()
