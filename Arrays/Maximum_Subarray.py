                                              ***Problem:***

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
   
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

                                               ***Code:***

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        total = float('-inf')
        
        for num in nums:
            sum = max(num, sum + num)
            total = max(total, sum)
        
        return total

                                            ***Explanation:***

nums = [-2,1,-3,4,-1,2,1,-5,4].

Initialization: sum = 0, total = float('-inf')
Iteration:
num = -2: sum = max(-2, 0 + -2) = -2, total = max(-inf, -2) = -2
num = 1: sum = max(1, -2 + 1) = 1, total = max(-2, 1) = 1
num = -3: sum = max(-3, 1 + -3) = -2, total = max(1, -2) = 1
num = 4: sum = max(4, -2 + 4) = 4, total = max(1, 4) = 4
num = -1: sum = max(-1, 4 + -1) = 3, total = max(4, 3) = 4
num = 2: sum = max(2, 3 + 2) = 5, total = max(4, 5) = 5
num = 1: sum = max(1, 5 + 1) = 6, total = max(5, 6) = 6
num = -5: sum = max(-5, 6 + -5) = 1, total = max(6, 1) = 6
num = 4: sum = max(4, 1 + 4) = 5, total = max(6, 5) = 6

Result: return total is 6.

---> Time Complexity: O(n)
---> Space Complexity: O(1)
