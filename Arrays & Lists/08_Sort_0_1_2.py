n=int(input())
for i in range(n):
    amazing=(input())
    list1=[int(x) for x in input().split()]
    sort_list1=sorted(list1)
    for j in range(len(sort_list1)):
        print(sort_list1[j],end=" ")
    print()