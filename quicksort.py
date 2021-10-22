# 1. Quick sort method divides the array in to two part and middle element as pivot. 
# 2. Now left handside of the pivot element will contain elements smaller than the pivot element. 
# 3. Right handside of the pivot element will contain elements greater than pivot element.
# 4. There are two types of partition schemes available for quick sort. 
#    - Hoare partition scheme (start element pivot)
#    - Lomuto partition scheme (end elmement pivot)
# 5. Big O complexity O(n^2).
def swap(x,y,num_list):
    temp = num_list[a]
    num_list[a] =  num_list[b]
    num_list[b] = temp
    


def partition(num_list):
    pivot_index = 0
    pivot = num_list[0]

    start = pivot_index + 1
    end = len(num_list)-1
    while num_list[start] <= pivot:
        start+=1

    while num_list[end] >= pivot:
        end-=1

    if start < end:
        swap(start, end, num_list)

def quick_sort(num_list):
    partition(num_list)
    






elements = [2,5,9,7,55,66,4,2,33,51,65,25,11,64]
quick_sort(elements)
print(elements)