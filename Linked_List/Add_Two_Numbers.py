                          *** Problem ***

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

                        *** Code ***

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 != None or l2 != None) or carry:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next

Output: [7,0,8]

                        *** Explanation ***

val = 0.
carry = 0.

11.val = 2, l2.val = 5.
sum = 2 + 5 + 0 (carry) = 7.
carry = 7 // 10 = 0.
val = 7 % 10 = 7 
list = [7], carry = 0

l1.val = 4, l2.val = 6.
sum = 4 + 6 + 0 (carry) = 10.
carry = 10 // 10 = 1.
val = 10 % 10 = 0 
list = [7, 0], carry = 1

l1.val = 3, l2.val = 4.
sum = 3 + 4 + 1 (carry) = 8.
carry = 8 // 10 = 0.
val = 8 % 10 = 8
list = [7, 0, 8], carry = 0

Output: [7, 0, 8]

---> Time Complexity: O(n)
---> Space Complexity: O(n)
