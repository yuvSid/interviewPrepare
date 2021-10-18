import json

# 2037. Minimum Number of Moves to Seat Everyone - # Easy
# There are n seats and n students in a room. You are given an array seats of length n, 
# where seats[i] is the position of the ith seat. You are also given the array students 
# of length n, where students[j] is the position of the jth student.
# You may perform the following move any number of times:
#   Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
# Note that there may be multiple seats or students in the same position at the beginning.

# https://leetcode.com/contest/biweekly-contest-63/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        res = 0
        for stud, seat in zip(sorted(students), sorted(seats)): 
            res += abs(stud-seat)
        return res

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            seats_line = f_in.readline().rstrip()
            students_line = f_in.readline().rstrip()

            if not (seats_line and students_line):
                break
            seats = json.loads(seats_line)
            students = json.loads(students_line)

            exec = Solution()
            res = exec.minMovesToSeat(seats, students)    

            f_out.write(json.dumps(res) + '\n')
