                                  *** Problem ***

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

                              *** CODE ***

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        node_map = {}
        while temp is not None:
            if temp in node_map:
                return temp
            node_map[temp] = True
            temp = temp.next
        return None

Output: tail connects to node index 1

                          *** Explanation ***

temp = 3.
node_map = empty y.

Add 3 to node_map: {3: True}.
temp -> (2).

temp = 2.

Add 2 to node_map: {3: True, 2: True}.
temp -> (0).

temp = 0.

Add 0 to node_map: {3: True, 2: True, 0: True}.
temp -> (-4).

temp = -4.
Add -4 to node_map: {3: True, 2: True, 0: True, -4: True}.
temp -> (which points back to node 2 due to the cycle).

temp = 2.
Return -> 2.

---> Time Complexity: O(n)
---> Space Complexity: O(n)
