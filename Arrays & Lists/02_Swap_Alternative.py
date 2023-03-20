#You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
#You don't need to print or return anything, just change in the input array itself.

def swapAlternate(li, n) :
    
    length = len(li)
    i = 0
    for k in range(length//2):
        li[i],li[i+1]=li[i+1],li[i]
        i+=2
    print(*li,end=" ")
    print()



t=int(input())
while t>0:
    
    n=int(input())
    arr=[int(i) for i in input().split()]
    swapAlternate(arr, n)
    t-=1