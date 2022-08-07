import json

# 704. Binary Search - Easy
#
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def __init__(self):
        self.__nums = []
        self.__target = 0

    def search(self, nums: list[int], target: int) -> int:
        self.__nums = nums
        self.__target = target
        return self.__bin_search(0, len(nums)-1)

    def __bin_search(self, left:int, right:int) -> int:   
        if left >= right:
            if self.__nums[left] == self.__target:
                return left
            else:
                return -1
        
        mid = (left + right) // 2
        if self.__nums[mid] == self.__target:
            return mid
        elif self.__nums[mid] > self.__target:
            return self.__bin_search(left, mid - 1)
        else:
            return self.__bin_search(mid + 1, right)

# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         dict_val = {val: ind for ind, val in enumerate(nums)}
#         return -1 if target not in dict_val else dict_val[target]        

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            array_line = f_in.readline().rstrip()
            target_line =f_in.readline().rstrip()
            if not (array_line and target_line):
                break
            array = json.loads(array_line)
            target = int(target_line)

            exec = Solution()        
            res = exec.search(array, target) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
