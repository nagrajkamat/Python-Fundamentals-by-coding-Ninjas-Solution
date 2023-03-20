def Findunique(li, n) :
    
    for i in range(n):
        
        found=False
        for j in range(n):
            if i!=j and arr[i]==arr[j]:
                found=True
                break
        if not found:
            print(arr[i])
            break



t=int(input())
while t>0: 
    n=int(input())
    arr=[int(i) for i in input().split()]
    Findunique(arr, n)
    t-=10