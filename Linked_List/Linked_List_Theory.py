    *** Linked List ***

It is a linear data structure that can be visualized as a chain with different nodes connected, where each node represents a different element. The difference between arrays and linked lists is that, unlike arrays, the elements are not stored at a contiguous location.

		*** Creating a Linked List ***

class Node:    
	def __init__(self,value1, next1 =None):        
		self.value = value1      
		self.next = next1
	
y = Node(2)
print(y.value)

Output: 2

	*** Types of Linked Lists ***

Singly Linked Lists: 
		In a singly linked list, each node points to the next node in the sequence. Traversal is straightforward but limited to moving in one direction, from the head to the tail.

Doubly Linked Lists: 
		In this each node points to both the next node and the previous node, thus allowing it for bidirectional connectivity.

    *** Insert at the head of a Linked List ***
To insert a new node with a value before the head of the list, create a new node with the given value val pointing to the head. This node will be the new head of the linked list.
                                                                                          
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
def printLL(head):      --->Function to print the linked list
    while head is not None:
        print(head.data, end=" ")
        head = head.next
def insertHead(head, val):    --->Function to insert a new node at the head of the linked list
    temp = Node(val, head)
    return temp

if __name__ == "__main__":    --->Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100

head = Node(arr[0])    --->Creating a linked list with initial elements from the array
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

head = insertHead(head, val)    --->Inserting a new node at the head of the linked list

printLL(head)    --->Printing the linked list

Output: 100 12 8 5 7

  *** Delete Last Node of Linked List ***

The main intuition is to point the second last node to null to get the updated linked list. Hence, we will iterate till the second last node and make it point to NULL. 

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# Function to delete the tail of the linked list
def delete_tail(head):
    # Check if the linked list is empty or has only one node
    if head is None or head.next is None:
        return None
    # Create a temporary pointer for traversal
    temp = head

    # Traverse the list until the second-to-last node
    while temp.next.next is not None:
        temp = temp.next

    # Nullify the connection from the second-to-last node to delete the last node
    temp.next = None

    # Return the updated head of the linked list
    return head

# Function to print the linked list
def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

# Main function
if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7]

    # Create the linked list with nodes initialized with array values
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Delete the tail of the linked list
    head = delete_tail(head)

    # Print the modified linked list
    print_ll(head)

Output: 2 5 8

    *** Find the Length of a Linked List ***

The most naive method to find the length of a linked list is to count the number of nodes in the list by doing a traversal in the Linked list.

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# Function to calculate the length of a linked list
def length_of_linked_list(head):
    cnt = 0
    temp = head
    
    # Traverse the linked list and count nodes
    while temp is not None:
        temp = temp.next
        cnt += 1
  
    return cnt
# Main function
def main():
    arr = [2, 5, 8, 7]
    # Create a linked list
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    # Print the length of the linked list
    print("Length of the linked list:", length_of_linked_list(head))
main()

       Output: 4

      *** Search an element in a Linked List ***
To check if an element is present in the linked list, traverse the list and at every node, check whether the data matches the specified value val. If a match is found, return true; otherwise, after traversing the entire list, return false.

class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to check if a given element is present in the linked list
def check_if_present(head, desired_element):
    temp = head

    # Traverse the linked list
    while temp is not None:
        # Check if the current node's data is equal to the desired element
        if temp.data == desired_element:
            return 1  # Return 1 if the element is found

        # Move to the next node
        temp = temp.next

    return 0  # Return 0 if the element is not found in the linked list

# Main function
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3
    arr = [1, 2, 3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])

    val = 3  # Element to be checked for presence in the linked list

    # Call the check_if_present function and print the result
    print(check_if_present(head, val))

      Output: True
