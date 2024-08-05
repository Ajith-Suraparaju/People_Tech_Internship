                          *** Problem ***

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

                        *** Code ***

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            temp = temp.next
        if cnt == n:
            newhead = head.next
            head = None
            return newhead
        res = cnt - n
        temp = head

        while temp is not None:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        delNode = temp.next
        temp.next = temp.next.next
        delNode = None
        return head

Output: [1,2,3,5]

                          *** Explanation ***

head = [1 -> 2 -> 3 -> 4 -> 5]
n = 2

cnt = 0
cnt = 1 (node value 1)
cnt = 2 (node value 2)
cnt = 3 (node value 3)
cnt = 4 (node value 4)
cnt = 5 (node value 5)
cnt = 5 (total number of nodes)

res = cnt - n = 5 - 2 = 3

temp -> 1 (res = 3 - 1 = 2)
temp -> 2 (res = 2 - 1 = 1)
temp -> 3 (res = 1 - 1 = 0)

Output: [1 -> 2 -> 3 -> 5]

---> Time Complexity: O(n)
---> Space Complexity: O(1)
