import math

def character_coord_finder(coord, string):
    if coord >= (len(string)-1):
        new_coord = coord - (len(string)-1)
        return character_coord_finder(new_coord,string)
    else:
        new_coord = coord
        return new_coord

def tobaggan(rightjump,downjump):

    filepath = 'day03input.txt'
    treecounter = 0
    opencounter = 0
    with open(filepath,"r") as filenow:
        lineslist = filenow.readlines()
        yrange = len(lineslist) / downjump
        for i in range(1,yrange):
            if i*downjump < len(lineslist):
                line=lineslist[i*downjump]
                charactercoordprelim = i*rightjump
                xcoord = character_coord_finder(charactercoordprelim,line)
                character = line[xcoord]
                if character == '.':
                    opencounter +=1
                if character == '#':
                    treecounter +=1

    return treecounter

def main():
    print 'Final product: ',tobaggan(1,1) * tobaggan(3,1) * tobaggan(5,1) * tobaggan(7,1) * tobaggan(1,2)

        
if __name__ == "__main__":
    main()


