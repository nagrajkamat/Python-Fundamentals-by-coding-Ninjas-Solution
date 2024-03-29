#You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively,
#merge them into a third array/list such that the third array is also sorted

from sys import stdin
def merge(arr1, n, arr2, m) : 
    ans = (n + m) * [0]
    i = 0 
    j = 0 
    k = 0
    while i < n and j < m :
        if arr1[i] < arr2[j] :
            ans[k] = arr1[i]
            k += 1 
            i += 1 
        else : 
            ans[k] = arr2[j] 
            k += 1 
            j += 1 
    while i < n :
        ans[k] = arr1[i]
        k += 1
        i += 1
    while j < m :
        ans[k] = arr2[j]
        k += 1
        j += 1
    return ans 
def takeInput() :
    n = int(input()) 
    if n != 0: 
        arr = list(map(int, input().strip().split(" "))) 
        return arr, n
    return list(), 0
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ") 
    print()
    
t = int(input()) 
while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    ans = merge(arr1, n, arr2, m) 
    printList(ans, (n + m)) 
    
    t -= 1