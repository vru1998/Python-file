# -*- coding: utf-8 -*-
"""list assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OPx9KlYme7-Y2dH_rjTk1labP_mNPiOd
"""

#1.WAP to remove to find duplicates elements in list
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))

#2 WAP to sort the given list
numbers = [1, 3, 4, 2]
# Sorting list of Integers in ascending
print(numbers.sort())  
print(numbers)           
 
print(sorted(numbers)) 
print(numbers)

#3. WAP to create a list such that new list contains alternate even and odd from given list

# 4. Write a Python program to get the largest number from a list.
# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]


# printing the maximum element
print("Largest element is:", max(list1))

#6. Write a Python program to remove duplicates from a list.
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))

#7. Write a Python program to find the list of words that are longer than given words
# length in the list
def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
 
    # for loop to traverse the list
    for i in a:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
    print("The word with the longest length is:", temp,
          " and length is ", max1)
 
 
# Driver Program
a = ["one", "two", "third", "four"]
longestLength(a)

#8. Write a Python function that takes two lists and returns True if they have at least one
#common member..
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False
         
 
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))
 
a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]
print(common_member(a, b))

#12. Write a Python program to print the numbers of a specified list after removing even
#numbers from it.

 #list of numbers
list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

