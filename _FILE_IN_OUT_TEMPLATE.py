import json

#
# Template

class Solution:
    def someFunc(self, line)-> str:
        return str(line)    
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not (readen_line):
                break
            readen = json.loads(readen_line)

            exec = Solution()
            res = exec.someFunc(readen)    

            f_out.write(json.dumps(res) + '\n')
