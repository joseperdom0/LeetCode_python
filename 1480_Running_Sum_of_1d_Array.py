"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
Seen this question in a real interview before?
1/4
Yes
No
Accepted
1.7M
Submissions
2M
Acceptance Rate
86.6%"""

"""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        out = []
        total = 0
        for seq in range(1,len(nums)+1):
            print("seq",seq)
            total = 0
            for i in range(seq):
                print("i is:",i)
                print("value of nums[i] is",nums[i])
                
                total += nums[i]
                print("total", total)
            out.insert(seq, total)
        print(out)
        return out
            
           
        #return total
           #return +nums[i]
           
"""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        out = []
        total = 0
        for seq in range(1,len(nums)+1):
            total = 0
            for i in range(seq):
                total += nums[i]
            out.insert(seq, total)
        return out        


# LeetCode solution
class Solution2:
    def runningSum(self, nums: list[int]) -> list[int]:
        out = []
        out.append(nums[0])

        return out     


sol = Solution2()
nums = [1, 2, 3, 4]
print(sol.runningSum(nums))
