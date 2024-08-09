def linear(array,target):
    for index,value in enumerate(array):
        if value == target:
            print("we found the value",value)
            break
#array = [10,20,40,5,60,70]
array=list(map(int,input().split()))
target = int(input())
linear(array,target)
