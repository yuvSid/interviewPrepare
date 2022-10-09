#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>

// 16. 3Sum Closest - Medium
// Given an integer array nums of length n and an integer target, 
// find three integers in nums such that the sum is closest to target.
// Return the sum of the three integers.

class Solution {
public:
    int threeSumClosest(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        auto closest = std::accumulate(nums.begin(), std::next(nums.begin(), 3), 0);
        if (closest >= target)
            return closest;
        closest = std::accumulate(std::prev(nums.end(), 3), nums.end(), 0);
        if (closest <= target)
            return closest;

        for (auto i = nums.begin(); i<std::prev(nums.end(), 2); i++) {
            auto j = std::next(i, 1);
            auto k = std::prev(nums.end(), 1);

            while (j < k) {
                auto sums = *i + *j + *k;
                if (std::abs(target-sums) < std::abs(target-closest))
                    closest = sums;
                if (sums == target)
                    return closest;
                else if (sums < target)
                    j = std::next(j, 1);
                else
                    k = std::prev(k, 1);
            }
        }
        
        return closest;    
    }
};