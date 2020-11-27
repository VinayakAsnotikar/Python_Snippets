#Insert sort method.
def insertion_sort(unordered_list):
    #Takes in the list to be sorted as parameter.
    for i in range(1,len(unordered_list)):
        #We start from one since the iteration occurs upto the lenght of the list.
        j = i - 1
        #j is the position of the current element.
        #i is the position of the next element.
        next_element = unordered_list[i]

        while (unordered_list[j] > next_element) and (j >=0 ):
            #We swap the elements if the current element is larger than the next element.
            unordered_list[j+1] = unordered_list[j]
            j = j - 1
        #We move to the next element.
        unordered_list[j+1] = next_element
    #We print out the ordered_list but its name is still unordered_list
    print(unordered_list)