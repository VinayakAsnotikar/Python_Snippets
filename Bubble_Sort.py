#Bubble sort method.
def bubblesort(unordered_list):
    #Takes in the list to be sorted as a parameter.
    for num in range(len(unordered_list)-1,0,-1):
        #We iterate over the positions in the list.
        #We start with the last element and move leftwards, one step upto the first element.
        for idx in range(num):
            #We take a position 'idx' in the list to compare with the adjacent numbes.
            if unordered_list[idx] > unordered_list[idx+1]:
                #We swap the numbers if they're not in order.
                temp = unordered_list[idx]
                unordered_list[idx] = unordered_list[idx+1]
                unordered_list[idx+1] = temp
    #We print out the ordered list but retained its name which was 'unordered_lis'
    print(unordered_list)