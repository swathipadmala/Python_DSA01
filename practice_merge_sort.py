def merge_sort(array):
    if len(array)<=1:
        return array
    else:
        mid = len(array)//2
        left_merge = merge_sort(array[:mid])
        right_merge = merge_sort(array[mid:])
    return merge(left_merge,right_merge)
def merge(left,right):
    sorted_array = []
    i= j = 0

    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

arr = [2,4,3,45,78,0,90,45]
sorted_array = merge_sort(arr)
print(sorted_array)

