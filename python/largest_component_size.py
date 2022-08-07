from __future__ import annotations

import json
from itertools import islice

from time import time

# 952. Largest Component Size by Common Factor - Hard
# You are given an integer array of unique positive integers nums. Consider the following graph:
#     There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
#     There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.
#
# https://leetcode.com/problems/largest-component-size-by-common-factor/

class dsJoinSet:
    def __init__(self, cur_size: int = 0):
        self.parent = self
        self.size = cur_size
    
    def find(self):
        while not (self.parent is self.parent.parent):
            self.parent.parent = self.parent.parent.parent
            self.parent = self.parent.parent

        return self.parent
    
    def union(self, other: dsJoinSet) -> None:
        if self.find() == other.find():
            return # already in one union

        if self.find().size < other.find().size:
            other.union(self) # other must be parent
            return
        
        self.parent.size += other.parent.size
        other.parent.parent = self.parent


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        primes = []
        for check in range(2, int(max(nums)**0.5)):
            for inside in primes:
                if check % inside == 0:
                    break
            else: # common factor not found already inside
                primes.append(check)
        
        joins = [dsJoinSet() for _ in primes]

        primes_len = len(primes)
        for num in nums:
            found = False
            for i in range(primes_len): #find first factor
                if not num % primes[i]:
                    joins[i].find().size += 1
                    found = True
                    break
            
            for k in range(i, primes_len):
                if num % primes[k] == 0:
                    joins[i].union(joins[k])
                    while not num % primes[k]:
                        num //= primes[k]
                        
            if num > 1:
                primes.append(num)
                primes_len += 1
                joins.append(dsJoinSet())
                if not found:
                    joins[-1].find().size += 1
                else:
                    joins[i].union(joins[-1])

        return 0 #(max(joins, key=lambda dsjSet: dsjSet.size)).size

class SolutionSlow:
    def largestComponentSize(self, nums: list[int]) -> int:
        
        def largestCommonDev(a: int, b: int) -> int:
            while a and b:
                a, b = min(a, b), max(a, b) % min(a, b)

            return max(a, b)

        res = [dsJoinSet() for _ in nums] 
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if res[i].find() is res[j].find():
                    continue                        
                
                if largestCommonDev(num, nums[j]) > 1:
                    res[i].union(res[j])

        return (max(res, key=lambda dsjSet: dsjSet.size)).size
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            start_time = time()
            res = exec.largestComponentSize(json.loads(args_raw[0]))    
            print(str.format('Input length: {1}, Time spend: {0:.4}'.format(time()-start_time, len(json.loads(args_raw[0])))))
            f_out.write(json.dumps(res) + '\n')
