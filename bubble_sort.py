def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    return array

arr = [20,2,34,45,67]
bubble_sort(arr)
print("bubble sort is:",arr)