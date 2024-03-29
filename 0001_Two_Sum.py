# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#  
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#  
#
# Constraints:
#
#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.
#
#  
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# SOLUTIONS
# Brute Force approach
# Time Complexity O(n^2)
# Space Complexity O(1)


class Solution(object):
    def twoSum(self, nums: list[int], target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counter = 0
        for i in nums:
            print("i:", i)
            counter += 1
            for j in nums[counter::]:
                print("j:", j)

                if i + j == target:
                    print(i, j)
                    return nums.index(i), nums.index(j, counter)


# Runtime: 5122 ms, faster than 13.35% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 96.14% of Python3 online submissions for Two Sum.

class Solution2:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            print(hashmap)
            if difference in hashmap:
                return [i, hashmap[difference]]
            hashmap[nums[i]] = i



nums = [2, 7, 14, 11]
target = 13
solution = Solution()
solution2 = Solution2()
# print(solution.twoSum(nums, target))
print(solution2.twoSum(nums, target))

# Runtime: 153 ms, faster than 36.14% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 26.28% of Python3 online submissions for Two Sum.
