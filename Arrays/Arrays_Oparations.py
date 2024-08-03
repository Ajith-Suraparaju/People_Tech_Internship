An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.
Arr = [1,2,3,4,5,6,7]

***Create an Array in Python ***
Array in Python can be created by importing an array module. array(data_type, value_list) is used to create array in Python with data type and value list specified in its arguments

import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

*** Adding Elements to a Array ***
Elements can be added to the Python Array by using built-in insert() function. 
Based on the requirement, a new element can be added at the beginning, end, or any given index of array. append() is also used to add the value mentioned in its arguments at the end of the Python array. 

import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1, 4)
b.append(6)

Output: [1,4,2,3,6]

*** Accessing Elements from the Array ***
In order to access the array items refer to the index number. Use the index operator [ ] to access an item in a array in Python. The index must be an integer. 

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[3])

Output: 4

*** Removing Elements from the Array ***
Elements can be removed from the Python array by using built-in remove() function but an Error arises if element doesn’t exist in the set. Remove() method only removes one element at a time.
pop() function can also be used to remove and return an element from the array.

import array
arr = array.array('i', [1, 2, 3, 1, 5])
arr.pop(2)
arr.remove(1)

Output: [2,1,5]

*** Slicing of an Array ***
There are multiple ways to print the whole array with all the elements, but to print a specific range of elements from the array, we use Slice operation. Slice operation is performed on array with the use of colon(:). To print elements from beginning to a range use [:Index].

import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
print("\nSlicing elements in a range 3-8: ")
print(a[3:8])
print("\nElements sliced from 5th "
      "element till the end: ")
print(a[5:])

Output: Initial Array: 
[1 2 3 4 5 6 7 8 9 10]
Slicing elements in a range 3-8: 
array('i', [4, 5, 6, 7, 8])

Elements sliced from 5th element till the end: 
array('i', [6, 7, 8, 9, 10])
