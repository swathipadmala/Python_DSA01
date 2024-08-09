def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j]:
                array[i] ,array[j] = array[j], array[i]
    return array
arr = [19,3,45,68,4,56]
res=bubble_sort(arr)
print(res)