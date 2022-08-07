import json

# 278. First Bad Version - Easy
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
#  Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# https://leetcode.com/problems/first-bad-version/

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

if __name__ == '__main__':    
    first_bad = 0
    def isBadVersion(version):
        return version >= first_bad

    class Solution:
        def firstBadVersion(self, n):
            """
            :type n: int
            :rtype: int
            """
            if isBadVersion(1):
                return 1

            correct, bad = 1, n #bin search for pair of last correct and false commit
            while correct != bad-1:
                check = (correct + bad) // 2
                if isBadVersion(check):
                    bad = check
                else:
                    correct = check
            return bad
    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_readen = f_in.readline().rstrip()
            bad_readen = f_in.readline().rstrip()
            if not (n_readen and bad_readen):
                break
            n = int(n_readen)
            first_bad = int(bad_readen)

            exec = Solution()
            res = exec.firstBadVersion(n)    

            f_out.write(json.dumps(res) + '\n')
