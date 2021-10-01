
# Simple text editor
# https://www.hackerrank.com/challenges/simple-text-editor/problem
#
# 

def processCommands(queries) -> str :
    histStr = ['']
    lastLine = 0
    for eachQ in queries :
        oper = eachQ[0]
        if oper == '1' :
            histStr.append(histStr[lastLine] + eachQ[1])
            lastLine += 1
        elif oper == '2' :
            histStr.append(histStr[lastLine][: -int(eachQ[1])])
            lastLine += 1
        elif oper == '3' :
            print(histStr[lastLine][int(eachQ[1])-1])
        elif oper == '4' :
            histStr.pop()
            lastLine -= 1
            if lastLine < 0 :
                lastLine = 0

if __name__ == '__main__':
    n = int(input().rstrip())

    queries = []
    for _ in range(n) :
        queries.append(input().rstrip().split())
    
    processCommands(queries)