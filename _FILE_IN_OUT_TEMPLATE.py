import json

#
# Template

def someFunc(line: str)-> str:
    return line    
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not readen_line:
                break

            res = someFunc(readen_line) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
