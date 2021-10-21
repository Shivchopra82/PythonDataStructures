# 1.Binary search is used to search on the sorted array. 
# 2.It searchs by dividing the array in two parts and comparing the middle element with the element we want to search. 
# 3.It compares the middle element with the element we want to search.
# 4.If middle element< searching element then we take second half array and search again. 
# 5. If middle element> searching element then we take first half array and search again by same method. 
# 6.If middle element = search element then search is complement we return the middle element.
# 7.O(logn) big O complexit of binary search of binary search is logn.

def linear_search(num_list, val):
    for index, element in enumerate(num_list):
        if element == val:
            return index
    return "not found"


def bin_search(num_list, val):
    left = 0
    right = len(num_list)-1
    mid = 0
    while left<=right:
        mid = (left+right)//2
        mid_num = num_list[mid]
        if val == mid_num:
            return mid
        if val > mid_num:
            left = mid + 1
        else:
            right = mid - 1
    return "not found"

# This is the binary search function. It uses the principle of binary search described above.

def recursive_binary(num_list, val, left, right):
    if left > right:
        return -1
    
    mid = (left+right)//2
    mid_num = num_list[mid]
    if mid_num == val:
        return mid
    elif val > mid_num:
        left = mid + 1
    else:
        right = mid - 1
    
    return recursive_binary(num_list, val, left, right)
#  Recursive function is used when we want to search an element between given index numbers.   


nums = [12, 15, 17, 19, 21, 24, 45, 67]
search_element = 24

pos = bin_search(nums, search_element)
print(pos)

pos2 = recursive_binary(nums, search_element, 0 , len(nums)-1)
print(pos2)

