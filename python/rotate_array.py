import json

#
# Template

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """
            
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            readen_step = f_in.readline().rstrip()
            if not (readen_line and readen_step):
                break
            nums = json.loads(readen_line)
            step = json.loads(readen_step)

            exec = Solution()
            exec.rotate(nums, step)    

            f_out.write(json.dumps(nums) + '\n')
