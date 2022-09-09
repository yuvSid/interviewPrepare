import json
from itertools import islice

# 997. Find the Town Judge - Easy
#
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trusted = [[False, 0] for _ in range(n)]
        for el in trust:
            trusted[el[0]-1][0] = True
            trusted[el[1]-1][1] += 1

        for i, el in enumerate(trusted):
            if not el[0] and el[1] == n-1:
                return i+1

        return -1
           
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.findJudge(json.loads(args_raw[0]), json.loads(args_raw[1]))    

            f_out.write(json.dumps(res) + '\n')
