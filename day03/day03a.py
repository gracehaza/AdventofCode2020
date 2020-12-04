import math

def character_coord_finder(coord, string):
    if coord >= (len(string)-1):
        new_coord = coord - (len(string)-1)
        return character_coord_finder(new_coord,string)
    else:
        new_coord = coord
        return new_coord

def main():

    filepath = 'day03input.txt'
    treecounter = 0
    opencounter = 0
    with open(filepath,"r") as filenow:
        lineslist = filenow.readlines()

        for i in range(1,len(lineslist)):
            line=lineslist[i]
            coordjump = 3     
            charactercoordprelim = i*coordjump
            xcoord = character_coord_finder(charactercoordprelim,line)
            character = line[xcoord]
            if character == '.':
                opencounter +=1
            if character == '#':
                treecounter +=1

        print 'open spaces counter: ',opencounter
        print 'tree counter: ', treecounter
        
if __name__ == "__main__":
    main()


