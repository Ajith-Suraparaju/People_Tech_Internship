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

l = 7 -1 = 6, k = 3

when i = 6, 6 > 3
t = 7
j = 6, 6 > 0:
nums[6] = nums[5], = 6
nums[5] = nums[4], = 5
nums[4] = nums[3], = 4
nums[3] = nums[2], = 3
nums[2] = nums[1], = 2
nums[1] = nums[0], = 1, j > 0, (1 > 0)
nums[0] = t, = 7

nums = [7,1,2,3,4,5,6]

when i = 5, 5 > 3
t = 6
j = 6, 6 > 0:

nums = [6,7,1,2,3,4,5]

when i = 4, 4 > 3
t = 5
j = 6, 6 > 0:

nums [ 5,6,7,1,2,3,4]

when i = 3, 3 !> 3 loop end's

Output: [5,6,7,1,2,3,4]

---> Time Complexity: O(n*n) or O(n2)
---> Space Complexity: O(1)
