# 1. Optimized form of insertion sort.
# 2. In insertion sort if your lower elements or smaller elements are towards the end them swaps are in large number.
# 3. In this we take gap in the array of elements.
# 4. By using small arrays by introducing the gap an iterating over the elements in the gap we can reduce the comparison needed in insertionsort.
# 5. In the second loop we reduce the gap by one and keep reducin the gap by one .
# 6. The last loop has gap of one which means it is insertionsort with less numbers of comparisons. 
# 7. Performance variables
    # -O(nlog^2n) worst case
    # -O(nlogn) best case

def shell_sort(lst):
    size = len(lst)
    gap = size//2
    for i in range(gap, size)






    
elements = [1,2,5,6,4,9,22,11,25,36,24,25,29,28,27,30,36,15,0,25,64,95,15,46,25,35,369,54,695,262,364,621,000,264,6775,41]
shell_sort(elements)
print(elements)