                                      *** Problem ***

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

                                  *** Code ***

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = len(nums)
        j = 0
        for i in range(a):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j +=1


                                *** Explanation ***

a = 5 
j = 0 
 (i = 0):
nums[0] is 0,  so j remains 0. Array: [0, 1, 0, 3, 12]

 (i = 1):
nums[1] is 1, which is non-zero.
Swap nums[1] with nums[0]: [1, 0, 0, 3, 12]
Increment j: j = 1

(i = 2):
nums[2] is 0, which is zero, so j remains 1.
List remains unchanged: [1, 0, 0, 3, 12]

(i = 3):
nums[3] is 3, which is non-zero.
Swap nums[3] with nums[1]: [1, 3, 0, 0, 12]
Increment j: j = 2

(i = 4):
nums[4] is 12, which is non-zero.
Swap nums[4] with nums[2]: [1, 3, 12, 0, 0]
Increment j: j = 3

Oitput: [1, 3, 12, 0, 0].

