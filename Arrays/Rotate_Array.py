                                      *** Problem ***

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

                                  *** Code ***

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums) - 1
        for i in range(l , k, -1):
            t = nums[l]
            for j in range(l, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = t

                                  *** Explanantion ***



---> Time Complexity: O(n*n) or O(n2)
---> Space Complexity: O(1)
