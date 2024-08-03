                                        *** Problem ***

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

                                            *** Code ***

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j +=1
        return j

                                          *** Explanation ***

j = 0
nums = [3, 2, 2, 3]

(i = 0):
nums[0] is 3, which is equal to val.
Do not update nums[j].
j remains 0.

(i = 1):
nums[1] is 2, which is not equal to val.
Update nums[j] to nums[1]:
nums[0] is updated to 2.
Increment j by 1:
j = 1
Current state of nums is [2, 2, 2, 3].

(i = 2):
nums[2] is 2, which is not equal to val.
Update nums[j] to nums[2]:
nums[1] is updated to 2.
Increment j by 1:
j = 2
Current state of nums is [2, 2, 2, 3].

(i = 3):
nums[3] is 3, which is equal to val.
Do not update nums[j].
j remains 2.

Output: 2

