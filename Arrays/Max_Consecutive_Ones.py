                                            *** Problem ***

Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

                                            *** Code ***

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count= count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
                
        return max(max_count,count)


                                            *** Explanation ***

nums = [1, 1, 0, 1, 1, 1].
max_count = 0
count = 0

First element (1):
i = 1
i == 1 is True, so increment count: count = 1
Current state: max_count = 0, count = 1

Second element (1):
i = 1
i == 1 is True, so increment count: count = 2
Current state: max_count = 0, count = 2

Third element (0):
i = 0
i == 0 is False, so update max_count and reset count:
max_count = max(max_count, count) = max(0, 2) = 2
count = 0
Current state: max_count = 2, count = 0

Fourth element (1):
i = 1
i == 1 is True, so increment count: count = 1
Current state: max_count = 2, count = 1

Fifth element (1):
i = 1
i == 1 is True, so increment count: count = 2
Current state: max_count = 2, count = 2

Sixth element (1):
i = 1
i == 1 is True, so increment count: count = 3
Current state: max_count = 2, count = 3


max_count = max(max_count, count) = max(2, 3) = 3

OutPut: max_count = 3, count = 3

---> Time Complexity: O(n)
---> Space Complexity: O(1).
