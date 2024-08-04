                            *** Problem ***

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

                          *** Code ***

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head  
        stack = []   
        while temp is not None:
            stack.append(temp.val) 
            temp = temp.next        
        temp = head  

        while temp is not None:
            temp.val = stack.pop()  
            temp = temp.next
           
        return head  

  Output: [5,4,3,2,1]

                          *** EXPLANATION ***

Pop 5: 5 -> 2 -> 3 -> 4 -> 5 -> None
Pop 4: 5 -> 4 -> 3 -> 4 -> 5 -> None
Pop 3: 5 -> 4 -> 3 -> 4 -> 5 -> None
Pop 2: 5 -> 4 -> 3 -> 2 -> 5 -> None
Pop 1: 5 -> 4 -> 3 -> 2 -> 1 -> None

---> Time Complexity: O(n)
--- Space Complexity: O(1)
