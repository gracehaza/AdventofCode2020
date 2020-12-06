

filepath = 'day05input.txt'

def x_or_y(low_str,high_str,min,max,coord,digits,offset,string):
    if coord == digits + offset:
        returnvalue = min
        return returnvalue
    if string[coord] == low_str:
        max = max - 2 ** (digits - coord + offset - 1)
        return x_or_y(low_str,high_str,min,max,coord+1,digits,offset,string)
    if string[coord] == high_str:
        min = min + 2 ** (digits - coord + offset - 1)
        return x_or_y(low_str,high_str,min,max,coord+1,digits,offset,string)
    coord =+1
        
def main():
    with open(filepath,"r") as filenow:
        lineslist = filenow.readlines()
        highestseatID = 0
        seat_ids = []
        for i in range(0,len(lineslist)):
            line = lineslist[i]
            row_coord = x_or_y('F','B',0,127,0,7,0,line)
            column_coord = x_or_y('L','R',0,7,7,3,7,line)
            seat_id = row_coord*8 + column_coord
            seat_ids.append(seat_id)
            if seat_id > highestseatID:
                highestseatID = seat_id
        seat_ids.sort()

        missing_seats = []

        for i in range (0, 927):
            number_found = False
            for j in range (0, len(seat_ids)):
                if i == seat_ids[j]:
                    number_found = True
            if number_found == False:
                missing_seats.append(i)

        for i in range (0, 927):
            minusneighbor = True
            plusneighbor = True
            first = missing_seats[0]
            last = missing_seats[len(missing_seats)-1]
            for j in range (1, len(missing_seats)-1):
                if i == missing_seats[j] and i+1 != missing_seats[j+1]:
                    plusneighbor = False
                    if i == first and plusneighbor == False:
                        print 'your seat no.: ', i

            for j in range (0, len(missing_seats)):
                if i == missing_seats[j] and i-1 != missing_seats[j-1]:
                   minusneighbor = False
                   if i == last and minusneighbor == False:
                       print 'your seat no.: ',i
        
         
        

if __name__ == "__main__":
    main()
