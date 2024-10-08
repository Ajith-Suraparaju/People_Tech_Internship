                                  *** Problem ***

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

                                *** Code ***

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        for i in nums2:
            nums1[m] = i
            m += 1
        nums1.sort()
  
                              *** Explanation ***

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Appending Elements from nums2 to nums1:
Iteration 1: nums1[3] = 2, m becomes 4
nums1 = [1, 2, 3, 2, 0, 0]

Iteration 2: nums1[4] = 5, m becomes 5
nums1 = [1, 2, 3, 2, 5, 0]

Iteration 3: nums1[5] = 6, m becomes 6
nums1 = [1, 2, 3, 2, 5, 6]

Sorting nums1:
After sorting, 

Output: nums1 = [1, 2, 2, 3, 5, 6]

---> Time complexity: O((m+n)log(m+n))
---> Space Complexity: O(1)
