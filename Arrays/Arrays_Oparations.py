*** Array ***
An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.
Arr = [1,2,3,4,5,6,7]

***Create an Array in Python ***
Array in Python can be created by importing an array module. array(data_type, value_list) is used to create array in Python with data type and value list specified in its arguments
 
import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

Output: [1,2,3]

*** Updating Elements in a Array ***
In order to update an element in the array we simply reassign a new value to the desired index we want to update.

import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
arr[2] = 6    ---> updating the value (6) at the particular index(2)
arr[4] = 8    ---> updating the value (8) at the particular index(4)

Output: [1, 2, 6, 1, 8, 5]

*** Adding Elements to a Array ***
Elements can be added to the Python Array by using built-in insert() function. 
Based on the requirement, a new element can be added at the beginning, end, or any given index of array. append() is also used to add the value mentioned in its arguments at the end of the Python array. 

import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1, 4)   ---> it inserts the value (4) at index (1)
b.append(6)      ---> It inserts the value (6) at the end of the array

Output: [1,4,2,3,6]

*** Accessing Elements from the Array ***
In order to access the array items refer to the index number. Use the index operator [ ] to access an item in a array in Python. The index must be an integer. 

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[3])     ---> to access the value at particular index(3)

Output: 4

*** Removing Elements from the Array ***
Elements can be removed from the Python array by using built-in remove() function but an Error arises if element doesn’t exist in the set. Remove() method only removes one element at a time.
pop() function can also be used to remove and return an element from the array.

import array
arr = array.array('i', [1, 2, 3, 1, 5])
arr.pop(2)    ---> it deletes the value at that particular index(2)
arr.remove(1)    ---> it deletes the first occurring value(1) from the array

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
print(a[3:8])        ---> to print the values from the index (3) to index (8).
print("\nElements sliced from 5th "
      "element till the end: ")
print(a[5:])        ---> to print the value from index (5) to rest of the values in an array

Output: Initial Array: 
[1 2 3 4 5 6 7 8 9 10]
Slicing elements in a range 3-8: 
array('i', [4, 5, 6, 7, 8])

Elements sliced from 5th element till the end: 
array('i', [6, 7, 8, 9, 10])

*** Searching Element in an Array ***
In order to search an element in the array we use a python in-built index() method.

import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print(arr.index(2))    ---> This function returns the index of the first occurrence of value mentioned in arguments.

Output: 1

*** Counting Elements in a Array ***
In order to count elements in an array we need to use count method.

import array
my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = my_array.count(2)    ---> it counts to the total number of values(2) present in the array.

Output: 3

*** Reversing Elements in a Array ***
In order to reverse elements of an array we need to simply use reverse method.

import array
my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.reverse()    ---> it reverses the array from right to left

Output: [5, 4, 3, 2, 1]

*** Extend Element from Array ***

An array is used to store multiple values or elements of the same datatype in a single variable.

import array as arr 
a = arr.array('i', [1, 2, 3,4,5])
a.extend([6,7,8,9,10])     ---> to insert the multiple values at the end of an array.

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


