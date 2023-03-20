def triplesum(list1,sum):
    sum_time=0
    a=len(list1)
    for i in range(0,a):
        for j in range(i+1,a):
            for k in range(j+1, a):
                if list1[i] + list1[j]+list1[k]==sum:
                    sum_time+=1
            
    print(sum_time)

n=int(input())
for i in range(n):
    amazing1=int(input())
    if amazing1!=0:
        list = [int(x) for x in input().split()]
    X=int(input()) 
    if amazing1!=0 :
        triplesum(list,X)
    else:
        print(0)