n=int(input())
start=1
end=2*n+1
mid=n+1
row=1
while(row<=n):
    column=1
    while column<=(2*n+1):
        if column==start or column==end or column==mid:
            print("*",end='')
        else:
            print("0",end="")
        column=column+1
    start=start+1
    end=end-1
    row=row+1
    print()

# Output -
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000    