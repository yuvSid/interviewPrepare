import json
from itertools import islice

# 155. Min Stack - # Easy
# Design a stack that supports push, pop, top, 
# and retrieving the minimum element in constant time.
# Implement the MinStack class:
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
#
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        self.__stack.append((val, val if not self.__stack else min(val, self.__stack[-1][1])))    

    def pop(self) -> None:
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1][0]

    def getMin(self) -> int:
        return self.__stack[-1][1]

class Solution:
    def exec(self, arg_1, arg_2)-> list:
        obj = None
        res = []
        for i, command in enumerate(arg_1):
            if command == "MinStack":
                obj = MinStack()
                res.append(None)
            elif command == 'push':
                obj.push(arg_2[i][0])
                res.append(None)
            elif command == 'pop':
                obj.pop()                
                res.append(None)
            elif command == 'top':
                res.append(obj.top())
            elif command == 'getMin':
                res.append(obj.getMin())
            else:
                assert('must not be here')
                break
    
        return res

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.exec(json.loads(args_raw[0]), json.loads(args_raw[1]))    

            f_out.write(json.dumps(res) + '\n')
