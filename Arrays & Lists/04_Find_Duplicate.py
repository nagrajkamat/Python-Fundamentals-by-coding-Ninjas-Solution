# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). 
# Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, 
# there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.

N = int(input())
k=0
while k<N:
    n = int(input())
    li = [int(x) for x in input().split()]
    new_li = li.copy()
    for i in range(n):
        new_li[i] = -1
        if li[i] in new_li:
            print(li[i])
            break
    k+=1
