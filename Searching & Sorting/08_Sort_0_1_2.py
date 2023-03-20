#You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s.
#Write a solution to sort this array/list in a 'single scan'.
#'Single Scan' refers to iterating over the array/list just once or to put it in other words,
#you will be visiting each element in the array/list just once.

from sys import stdin
def sort012(arr, n) :
    nextZero = 0
    nextTwo = (n - 1) 
    i = 0 
    while i <= nextTwo :
        if arr[i] == 0 :
            temp = arr[nextZero]
            arr[nextZero] = arr[i] 
            arr[i] = temp
            i += 1
            nextZero += 1
        elif arr[i] == 2 :
            temp = arr[nextTwo] 
            arr[nextTwo] = arr[i] 
            arr[i] = temp
            nextTwo -= 1
        else : 
            i += 1 
def takeInput() : 
    n = int(input().rstrip())
    if n == 0 :
        return list(), 0 
    arr = list(map(int, input().rstrip().split(" ")))
    return arr, n
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print() 
t = int(input())
while t > 0 :
    arr, n = takeInput() 
    sort012(arr, n)
    printList(arr, n) 
    t -= 1

