                              *** Problem ***

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

                          *** Code ***


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        mid = count // 2 + 1
        temp = head
        while temp is not None:
            mid = mid -1
            if mid == 0:
                break
            temp = temp.next
        return temp

Output: [3,4,5]

                              *** Explanation ***

head = 1.
count = 0.

Counting the Nodes:
temp = 1. count= 1.
temp = 2. count = 2.
temp = 3. count = 3.
temp = 4. count = 4.
temp = 5. count = 5.
temp = None. 

mid = count // 2 + 1, -> 5 // 2 + 1 = 3.

mid = 2, and temp = 2.
mid = 1, and temp = 3.
mid = 0. 

Output: [3, 4, 5].

---> Time Complexity: O(n)
---> Space Complexity: O(1)
