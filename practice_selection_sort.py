def selection_sort(array):
    for i in range(len(array)):
        min_value = i
        for j in range(i+1,len(array)):
            if arr[j] < arr[min_value]:
                min_value = j
        array[min_value],array[i] = array[i],array[min_value]

arr = [2,45,34,69,4,344]
selection_sort(arr)
print(arr)
