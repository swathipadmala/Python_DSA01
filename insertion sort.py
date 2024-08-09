def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = key
arr = [20,35,56,78,3,5]
insertion_sort(arr)
print("insertion sort:",arr)

