def binary(array,target):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif array[mid]< target:
            left = mid+1 
        else:
            right = mid-1

array = [2,4,8,9,10,12]
target = 4
res = binary(array,target)
print(res)
