
#
# Template

#INPUT:

def funcName() :
    pass
    
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    frptr = open('./OUTPUT/IN', 'r')
    fptr = open('./OUTPUT/OUT', 'w')
    
    lineNums = frptr.readline()
    lineTarget = frptr.readline()
    while lineNums and lineTarget :
        nums = list(map(int, lineNums.rstrip()[1 : -1].split(sep = ',')))
        target = int(lineTarget.rstrip())

        result = 0 # TODO add func here
        fptr.write(str(result) + '\n')

        lineNums = frptr.readline()
        lineTarget = frptr.readline()

    #fptr.write(str(result) + '\n')
    frptr.close()
    fptr.close()
