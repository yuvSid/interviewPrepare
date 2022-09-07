import json
from itertools import islice
#
# Template

class Solution:
    def someFunc(self, line)-> str:
        return str(line)    
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.someFunc(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
