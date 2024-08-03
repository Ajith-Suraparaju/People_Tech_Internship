***Problem:**

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

***Code:***
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

***Explanation:***
nums = [3,2,4], target = 6

outer loop 1:
(i = 0), nums[i] = 3.
(j = 1): nums[j] = 2.
nums[i] + nums[j] == target:
3 + 2 is not equal to 6

(j = 2): nums[j] = 4.
nums[i] + nums[j] == target:
3 + 4 is not equal to 6

Outer loop 2:
(i = 1):nums[i] =2
(j = 2): nums[j] = 4.
nums[i] + nums[j] == target:
2 + 4 is equal to 6.

Output:
The function returns [1, 2].

