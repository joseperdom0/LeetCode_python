# 9. Palindrome Number
# Easy
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
#
# Constraints:
#
#     -2^31<= x <= 2^31- 1
#
#
# Follow up: Could you solve it without converting the integer to a string?

# BRUTE FORCE
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        palindrome = True
        for i in range(len(number)//2):
            print(number[i], number[-(i + 1)])
            if number[i] != number[-(i + 1)]:
                palindrome = False
                break
        return palindrome


# One liner
class SolutionTwo:
    def isPalindrome(self, x: int) -> bool:
        stringify = str(x)
        if stringify[::] == stringify[::-1]:
            return True
        return False

# Runtime:58 ms, faster than 96.34% of Python3 online submissions for Palindrome Number.
# Memory Usage:13.9 MB, less than 16.46% of Python3 online submissions for Palindrome Number.

class SolutionThree:
    def isPalindrome(self, x: int)-> bool:

        if x > 0:
            order_of_magnitude = math.floor(math.log10(x))
            num_array = []
            remainder = x
            for i in range(order_of_magnitude + 1):
                difference = 10 ** (order_of_magnitude - i)
                number = remainder // difference
                remainder = remainder - (number * difference)
                num_array.append(number)
            print(num_array)
            if num_array[::] == num_array[::-1]:
                return True
        return False


class Solution4:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        while x > 0:
            reversed = (reversed * 10) + (x % 10)
            print(reversed)
            x = x//10


x = 103
x2 = 10
solution = Solution4()
solution.isPalindrome(x)
