# Sorting is the method for arranging the list of numbers in desired order.
#2.Time complexity is order of n^2 
def bub_sort(num_list):
    size = len(num_list)
    for i in range(size-1):
        for j in range(size-1-i):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp



ele = [2,5,6,4,9,55,44,88,22,15,36,15,25,26,27,95,15,65,85,56,55]
bub_sort(ele)
print(ele)