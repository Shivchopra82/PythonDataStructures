# 1. Quick sort method divides the array in to two part and middle element as pivot. 
# 2. Now left handside of the pivot element will contain elements smaller than the pivot element. 
# 3. Right handside of the pivot element will contain elements greater than pivot element.
# 4. There are two types of partition schemes available for quick sort. 
#    - Hoare partition scheme (start element pivot)
#    - Lomuto partition scheme (end elmement pivot)
# 5. Big O complexity O(n^2).



def swap(x,y,num_list):
    temp = num_list[x]
    num_list[x] =  num_list[y]
    num_list[y] = temp
    


def partition(num_list,start, end):
    pivot_index = start
    pivot = num_list[pivot_index]
    while start < end:
        while start < len(num_list) and num_list[start] <= pivot:
            start+=1

        while num_list[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, num_list)
    swap(pivot_index, end, num_list)
    return end

    # This function divides the array in to two partion by sorting it according to pivot point as explained above.



def quick_sort(num_list, start, end):
    if start < end:
        key = partition(num_list, start, end)
        quick_sort(num_list, start, key-1)   
                                    #continuing process for left partition.
        quick_sort(num_list, key+1, end)   
                                    #continuing same process for right partition.
    # This is the main quick sort function which sorts the array by partitioning it using the partition function.



elements = [52,2,5,9,7,55,66,4,2,33,51,65,25,11,64]
quick_sort(elements, 0, len(elements)-1)
print(elements)
