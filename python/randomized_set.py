import json
from itertools import islice
from random import randint

# Implement the RandomizedSet class:
#     RandomizedSet() Initializes the RandomizedSet object.
#     bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#     bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#     int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        last_num = self.nums.pop()
        if last_num != val:
            self.nums[self.pos[val]] = last_num
            self.pos[last_num] = self.pos[val]
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class Solution:
    def exec(self, arg_1, arg_2)-> list:
        obj = None
        res = []
        for i, command in enumerate(arg_1):
            if command == "RandomizedSet":
                obj = RandomizedSet()
                res.append(None)
            elif command == 'insert':
                res.append(obj.insert(arg_2[i][0]))
            elif command == 'remove':
                res.append(obj.remove(arg_2[i][0]))
            elif command == 'getRandom':
                res.append(obj.getRandom())
            else:
                assert('must not be here')
                break
    
        return res

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.exec(json.loads(args_raw[0]), json.loads(args_raw[1]))    

            f_out.write(json.dumps(res) + '\n')
