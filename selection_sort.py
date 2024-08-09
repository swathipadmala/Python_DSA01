def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

data = [1,4,3,5,7,9,30,2,20]

print("list is before sorting",data)
selection_sort(data)
print("list is after sorted",data)

