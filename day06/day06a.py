import string
filepath = 'day06input.txt'

def look_at_questions(begin,end):
    with open(filepath,"r") as filenow:
        lineslist=filenow.readlines()
        questions=list(string.ascii_lowercase)
        yesquestions=[]
        for k in range(0, len(questions)):
            valid = False
            for j in range(begin,end):
                line=lineslist[j]
                bool = line.find(questions[k])
                if bool != -1:
                    valid = True
            yesquestions.append(valid)
        return yesquestions
        
def main():
    with open(filepath,"r") as filenow:
        sumofcounts = 0
        lineslist = filenow.readlines()
        min = 0
        for i in range(0,len(lineslist)):
            line = lineslist[i]
            if line =="\n":
                max = i
                yesarray = look_at_questions(min, max)
                thisgroupyes = 0

                for l in range(0,len(yesarray)):
                    if yesarray[l] == True:
                        thisgroupyes += 1
                sumofcounts += thisgroupyes
                min = i

            if i == len(lineslist)-1:
                lastyesarray = look_at_questions(max, len(lineslist))
                lastgroupyes = 0
                for m in range (0,len(lastyesarray)):
                    if lastyesarray[m] == True:
                        lastgroupyes += 1
                sumofcounts += lastgroupyes

    print 'sum of counts: ',sumofcounts



if __name__ == "__main__":
    main()
