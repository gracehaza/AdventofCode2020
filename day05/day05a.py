
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
        for i in range(0,len(lineslist)):
            line = lineslist[i]
            row_coord = x_or_y('F','B',0,127,0,7,0,line)
            column_coord = x_or_y('L','R',0,7,7,3,7,line)
            seat_id = row_coord*8 + column_coord
            if seat_id > highestseatID:
                highestseatID = seat_id
        print 'highest seat ID: ', highestseatID

if __name__ == "__main__":
    main()
