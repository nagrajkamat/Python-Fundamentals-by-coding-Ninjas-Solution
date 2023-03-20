#1 What will be the output of the code?
a = 5,6,7
print(a[1:])
answer = (6,7)


#2 What will be the output of follwing code?
a = 5,6,7
a[2] = 9 
print(a)
answer = Error

#3 What will be the output of following code?
a = 1,2
b = (4,5)
d = (a,b)
print(d[0]
answer = (1,2)


#4 What will be the output of follwing code?
a = 1,2
b = (4,5)
d = a+b
print(d[2])
answer = (4,5)

#5 What will be the output of following code?
a = (“ab”,”abc”,”def”)
print(min(a)
answer = ab

#6What will be the output of following code?
def multiply(a,b,c,*more):
    value = a*b*c
    for i in more:
        value = value * i
    return value
V = multiply(1,2,3,4,5)
print(V)
answer = 120

#7 what will the output of code?
def sum_multiply(a,b,*more):
    sum_value = a+b
    m_value = a*b
    for i in more:
        sum_value += i
        m_value*=i
    return sum_value,m_value
s_m = sum_multiply(2,3,4)
print(s_m)
answer = (9, 24)

#8 What will be the output of following code?
d = {1:2, “abc”:5, “def”:7}
print(d[0])
answer = Error

#9 what will be the output of the code?
d = {1:2, “abc”:5, “def”:7}
print(d.get(0,5))
answer = 5

#10 What will be the output of following code?
d = {1:2, “abc”:5, “def”:7}
if 2 in d:
    print(‘Present’)
else:
    print(‘Not Present’)
answer = Not Present

#11 What will be the output of following code?
a = {1:2,’list’:[1,2],3:5}
b = {4:5,3:7}
a.update(b)
print(a[3])
answer = 7

#12 What will be the output of following code?
a = {1:2,’list’:[1,2],3:5}
a.pop(‘list’)
a[‘list’] = [3,5]
print(a[‘list’])
answer = [3,5]

#13 What will be the output of following code?
s = {1,2,3,5,4,2,3,1}
print(len(s),end= “ “)
s.add(4)
s.add(3)
print(len(s))
answer = {1, 2, 3, 4, 5}

#14 What will be the output of following code?
s = {}
s.add(4)
s.add(4)
print(len(s))
answer = Error

