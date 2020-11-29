#Selection sort method.
def selection_sort(unordered_list):
    #The function takes the list to be sorted as a parameter.
    for idx in range(len(unordered_list)):
        #We take the position 'idx' for the lenght of the list.
        min_idx = idx
        #We assume the position of the smallest element is idx hence min_idx.
        for j in range(idx+1, len(unordered_list)):
            if unordered_list[min_idx] > unordered_list[j]:
                #We check if it is indeed the smallest number and record its position 
                min_idx = j
        #We swap the elements so that they can be in order
        unordered_list[idx], unordered_list[min_idx] = unordered_list[min_idx], unordered_list[idx]
    #We print out the sorted list but we retained its name as unordered_list
    print(unordered_list)