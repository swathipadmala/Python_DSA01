def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
        
        less_pivot_element = [x for x in array[1:] if x <= pivot ]
        greater_pivot_element = [x for x in array[1:] if x > pivot]
    return quick_sort(less_pivot_element)+[pivot]+quick_sort(greater_pivot_element) 
   
arr = [2,43,23,56,76,345,890,456]
res = quick_sort(arr)
print(res)