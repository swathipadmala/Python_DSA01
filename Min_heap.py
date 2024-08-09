def left(k):
    return 2*k+1
def right(k):
    return 2*k+2
def min_heap(A,k):
    l = left(k)
    r = right(k)

    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    
    if r < len(A) and A[r] < A[smallest]:
        smallest = r

    
    if smallest != k:
        A[k],A[smallest] = A[smallest],A[k]

def build_min_heap(A):
    n = len(A)//2-1
    for i in range(n,-1,-1):
        min_heap(A,i)

A = [3,9,2,1,4,5]
build_min_heap(A)
print('Min Heap:', A)

