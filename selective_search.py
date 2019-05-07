import numpy as np
import math
# divide n elements of the input array into floor(n/5) groups.
def divide(arr):
    return [arr[i*5:(i+1)*5] for i in range(math.ceil(len(arr)/5))]
def insertion_sort(arr):
   for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j > -1 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1
        arr[j+1] = key
return arr
# find the median of given array by first insertion-sorting and picking the median.
def find_Median(arr):
    # insertion sort input array.
    sorted = insertion_sort(arr)
    
    # if there are an even number of medians, then by our convention, lower one is the median.
    median = math.floor(len(arr)/2)
    if len(arr) % 2 == 0:
        median = median - 1
        
    return sorted[median]
    # modified version of partition.
# use given input x as pivot.
def partition(A, p, r, x):
    # send given input x to the last of array to use it as pivot.
    i = p
    for j in range(p,r):
        if A[j] == x:
            break
        i = i + 1
    A[i], A[r] = A[r], A[i]
    
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i] # exchange A[i] with A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
def select(arr, p, r, i):
    group_size = 5
    n = len(arr)
    
    # base case : when there are less than 5 elements in input array, return ith element.
    if n <= group_size:
        sorted_arr = insertion_sort(arr) 
        return sorted_arr[i-1]
    
    # step_1 : divide the n elements of the input array into floor(n/5) groups of 5 elements each and 
    #at most one group with remaining elements.
    grouped_arr = divide(arr)
    
    # step_2 : find the median of each of ceiling(n/5) groups by insertion-sorting each group and then 
    #picking the median from the sorted list of groups.
    
    median_list=[]
    for z in range(len(grouped_arr)):
        median_list.append(find_Median(grouped_arr[z]))
    #print("Median_list is : " , median_list)
    # step_3 : use select() recursively to find the median of the floor(n/5) medians found in step 2.
    # if there are even number of medians, then by our convention, lower one is the median.
    median = math.floor(len(median_list)/2)
    if len(median_list) % 2 == 0:
        median = median - 1
    mom = select(median_list, 0, len(median_list)-1, median)
    #print("mom is: ", mom)
    
    # step_4 : partition the input array around the median-of-medians(mom).
    q = partition(arr, p, r, mom) #changed 2 and 3 params
    #print("q is: ", q)
    #print("partition number is: ", arr[q])
    #print("partitioned array: ", arr)
    k = q - p + 1
    #print("k is:", k, "p is: ", p)
    # step_5 : 
    if i == k: #if our number is equal to number next to mom
        return arr[q] #return pivot number
    elif i < k:
        newarr = arr[:q]
        newn = len(newarr)
        return select(newarr,0,newn-1,i)#select's params are arr, p, r, i
    else:
        newarr = arr[k:]
        newn = len(newarr)
        return select(newarr,0,newn-1,i-k)
def main():
    n = int(input("Give size of input list: "))
    k = int(input("Give n for the n-th number: "))
    input_arr = np.random.randint(0, 100, size = n)
    sorted_arr = insertion_sort(input_arr)
    kth_num = select(input_arr, 0, n-1, k)
    print(sorted_arr[k-1] == kth_num)