                                    *** Problem ***

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

                                    *** Code ***

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        for num in nums:
            if num < 0:
                nums[i] = num * num
            else:
                nums[i] = num * num
            i += 1
        return sorted(nums)

                                    *** Explanation ***

nums = [-4, -1, 0, 3, 10]
For -4, nums[0] becomes 16.
For -1, nums[1] becomes 1.
For 0, nums[2] becomes 0.
For 3, nums[3] becomes 9.
For 10, nums[4] becomes 100.

nums = [16, 1, 0, 9, 100]

sorted_nums = sorted([16, 1, 0, 9, 100])
sorted_nums = [0, 1, 9, 16, 100]

Output: [0, 1, 9, 16, 100]

---> Time Complexity: O(nlogn)
---> Space Complexity: O(n)
