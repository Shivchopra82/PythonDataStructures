# 1. In each iteration we compare the element with starting element and change the position accordingly. 
# 2. Thus in each iteration we have a sorted array on left handside and unsorted array on right hand side. 

def select_sort(lst):
    size = len(lst)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]


elements = [1,2,5,6,4,9,22,11,25,36,24,25,29,28,27,30,36,15,0,25,64,95,15,46,25,35,369,54,695,262,364,621,000,264,6775,41]
select_sort(elements)
print(elements)