from sys import stdin
def bubbleSort(arr, n) :
    for i in range(n - 1) :
        for j in range(n - i - 1) :
            if arr[j] > arr[j+1] :
                temp = arr[j] 
                arr[j] = arr[j + 1]
                arr[j + 1] = temp 
def takeInput() : 
    n = int(input().strip()) 
    if n == 0 : 
        return list(), 0
    arr = list(map(int, input().strip().split(" "))) 
    return arr, n
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ") 
    print() 
t = int(input().strip()) 
while t > 0 :
    arr, n = takeInput()
    bubbleSort(arr, n)
    printList(arr, n) 
    t-= 1











