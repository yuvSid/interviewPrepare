import json

#
# Template

def someFunc():
    pass    
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out :
        readen_line = f_in.readline().rstrip()
        while readen_line :
            lst = json.loads(readen_line)

            res = someFunc(lst) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
            readen_line = f_in.readline().rstrip()
