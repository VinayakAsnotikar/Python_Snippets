# Python_Snippets

## I] Random Code

1) [RandomPasswordGenerator.py](RandomPasswordGenerator.py): This is a basic python code to generate random 16 character passwords using letters (caps and small), numbers and symbols using random module.

2)[Simple_Calculator.py](Simple_Calculator.py): This is one of the shortest and simplest calculator program in python you could ever found. We will create a calculator that will add, subtract, divide, and multiply two numbers. We will run the program until we don’t want to exit using a while loop, so that we can calculate as many as calculations we want.

**************************************************************************************************************************************************

## II] Sorting Algorithms
A sorting algorithm is used to rearrange a given list or an array of elements in a defined order, either in increasing or decreasing order.

1) [Insertion_Sort.py](RandomPasswordGenerator.py): Simple python code for Insertion sort method.This sorting algorithm involves finding the right place for each element in the array. We begin by taking the first two elements and finding the position of each relative to the other. We then add the third element and compare it to the previous elements and find its position. Other elements are added gradually to the sorted list until the list is exhausted.

2) [Bubble_Sort.py](Bubble_Sort.py): Simple python code for Bubble sort method. This is quite similar to insertion sorting algorithm but differs in some ways. In this algorithm, we only compare adjacent elements and we then swap them if they are not in order. It is way much simpler to understand as compared to the previous algorithms.

3) [Selection_sort.py](Selection_sort.py): Simple python code for Selection sort method. Here, we get the smallest element in a list and take it to a copy list, then repeat the process for the remaining elements until all of the elements have been sorted in the list.

**************************************************************************************************************************************************

## III] Searching Algorithms
A searching algorithm is used to check the presence of an element in a list or array and displays the position of the element in the list or array or will return a False if it is non-existent in the list. 

This involves looking for a specific element in a list or array of elements. It detects its presence and will return a True or false if present or absent respectively. It can also return the position of the element in the list if it is present and return an ‘absent statement’ if it’s absent.

1) [Linear_searching.py](Linear_searching.py): This is one of the searching algorithms that involves sequentially going through every element in the list until the element is located and its position is enumerated. This method might take a long time to run if the list or array is quite long and the element being searched is deep in the array. This is the disadvantage of this method. However, this method is quite handy as it can search in an unsorted list unlike the other method of searching that we will come to later.

2) [Binary_searching.py](Binary_searching.py): This is a Searching algorithm that is quite different from its counterpart. It involves getting a sorted list and dividing it into two. Since it is sorted, the numbers are in order. We check if the number to be searched is larger or smaller than the middle number. If it is larger, we take the second half and if it is smaller we take the first half. We do this consequently until we find the element being searched. We then return its position in the list if it is present or return an ‘absent statement’ if it isn’t present in the list.
This algorithm will run faster than the linear search since it doesn’t iterate over every element in the list. However, this algorithm prerequisite is that the list should be sorted. You can sort the list inside the function but that will take up time too.

**************************************************************************************************************************************************