def linear(array,target):
    for i in range(len(array)):
        if array[i] == target:
            print(f"we found the value {i}")
            break
array = [2,4,5,6,7,8]
target = 6
linear(array,target)