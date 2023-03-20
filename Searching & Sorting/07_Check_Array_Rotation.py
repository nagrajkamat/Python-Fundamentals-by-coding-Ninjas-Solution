#You have been given an integer array/list(ARR) of size N.
#It has been sorted(in increasing order) and then rotated by some number 'K' (K is greater than 0) in the right hand direction.
#Your task is to write a function that returns the value of 'K', that means, the index from which the array/list has been rotated.

from sys import stdin 
def arrayRotateCheck(arr, n):
    for i in range(n - 1):
        if(arr[i] > arr[i + 1]):
            return (i + 1) 
    return 0 
def takeInput() : 
    n = int(input().rstrip()) 
    if n == 0:
        return list(), 0 
    arr = list(map(int, input().rstrip().split(" "))) 
    return arr, n
t = int(input().rstrip())
while t > 0 :
    arr, n = takeInput() 
    print(arrayRotateCheck(arr, n))
    
    t -= 1



