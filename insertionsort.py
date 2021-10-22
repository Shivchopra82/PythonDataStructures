#1.In this sorting method we select element one by one and place them on their right position.
#2.First we start by takin the first element as sorted array and ainserting the rest of the elements at their right positon. 
# 3. Performance variables.
#   * Worst-case performance O(n^2)
#   * Best-case performance O(n)
#   * Average-case performance O(n^2)

def insertionsort(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i-1
        while j>=0 and key < num_list[j]:
            num_list[j+1]  = num_list[j]
            j = j-1
        num_list[j+1] = key


numbers = [1,2,4,5,6,9,7,5,66,74,8,32,5,58,59,21,64,62,3,5,44,45]
insertionsort(numbers)
print(numbers)
