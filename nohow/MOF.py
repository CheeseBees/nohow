#MathematicOperationFunctions
def ii(inp,ind):
    #Integer index
    return int(str(inp)[ind])
def iis(inp,ind):
    #integer index to string
    return str(int(str(inp)[ind]))
def leastof(group):
    firsttime = True
    lowest = 0;
    for i in group:
        if firsttime == True:
            lowest = i
            firsttime = False
        if firsttime == False:
            if i < lowest:
                lowest = i
            else:
                continue
    return lowest
def longdiv(dvd,dvs,limit):
    #Long division - UNFINISHED
    nums = [0] * limit
    rem = 0
    full = 0
    p = 0
    print(" __________")
    print(str(dvs) + ")" + str(dvd))
    sys.stdout.write(" " * int(len(str(dvs))+1))
    for i in range(0,len(str(dvd))):
        nums[i] = ii(dvd,i)
        
    for i in range(0,len(str(dvd))):
        full = int(str(rem) + str(nums[i]))
        if full < dvs:
            rem = int(str(nums[i-1]) + str(nums[i]))
            sys.stdout.write("0")
        else:
            sys.stdout.write(str(full//dvs))
            rem = full%dvs
##        
##        print(str(dvs) + ")" + str(dvd))
##        rem = 0
##        step = [0] * limit
##        for i in range(0,len(str(dvd))-1):
##            fulldividend = ii(dvd,i) + rem
##            step[i] = str(fulldividend//int(str(dvs)))
##            rem = fulldividend % int(str(dvs))
##            print(":",rem)
##            if int(step[i]) == 0:
##                #sys.stdout.write
##                print(":" , " " * int(i+1) + step[i])
##            else:
##                print(str(fulldividend) + step[i])
##
