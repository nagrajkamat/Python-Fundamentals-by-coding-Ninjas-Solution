#You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. 
#Write a function to search this element in the given input array/list using 'Binary Search'. 
#Return the index of the element in the input array/list. 
#If the element is not present in the array/list, then return -1

from sys import stdin
def binarySearch(arr, n, x) : 
    start = 0;
    end = n - 1 
    mid = start
    while start <= end :
        mid = start + (end - start) // 2
        if arr[mid] > x :
            end = mid - 1
        elif arr[mid] < x :
            start = mid + 1 
        else : 
            return mid 
    return -1
def takeInput() :
    n = int(input())
    if n == 0 :
        return list(), 0
    arr = list(map(int, input().strip().split(" "))) 
    return arr, n
arr, n = takeInput()
t = int(input()) 
while t > 0 : 
    x = int(input().strip()) 
    print(binarySearch(arr, n, x)) 
    t -= 1