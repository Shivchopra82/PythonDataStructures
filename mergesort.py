# 1.This is basically the divide and conquer method.
# 2.This function devides the array in to two parts and again divivdes the individual part in to two parts and so on until it left with single element. 
# 3.After that it start merging all those parts(taking two at one time) by comparing the elements with each other. 
# 4.Python's time sort algorithm used this mergesort.
# 5.Performance O(nlogn).




def merge_sort(num_list):
    if len(num_list)<=1:
        return num_list
    mid = len(num_list)//2
    left = num_list[:mid]
    right = num_list[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, num_list)
    # This function do the dividing part of the algorithm.




def merge(a,b, num_list):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i=j=k=0

    while i<len_a and j<len_b:
        if a[i] <= b[j]:
            num_list[k]=a[i]
            i+=1
        else:
            num_list[k]=b[j]
            j+=1
        k+=1
    while i< len_a:
        num_list[k]=a[i]
        i+=1
        k+=1
    while j< len_b:
        num_list[k]=b[j]
        j+=1
        k+=1
    # This function merge all the divided parts of array in to the sorted array.





elements = [1,2,5,6,4,9,22,11,25,36,24,25,29,28,27,30,36,15,0,25,64,95,15,46,25,35,369,54,695,262,364,621,000,264,6775,41]
merge_sort(elements)
print(elements)