#Exercise 1-------------------------------------------------------------------
def fun(n):
    for x in range(1,n+1):
        yield x**2
n = int(input())
f = fun(n)
for q in f: print(q)
#Exercise 2-------------------------------------------------------------------
def fun(n):
    for x in range(1,n+1):
        if x%2==0:
            yield x
n = int(input())
even = fun(n)
for i in even: print(i)
#Exercise 3-------------------------------------------------------------------
def fun(n):
    for x in range(0,n+1):
        if x%3==0 and x%4==0:
            yield x
n = int(input())
this = fun(n)
for i in this: print(i)
#Exercise 4-------------------------------------------------------------------
def fun(a,b):
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
this = fun(a,b)
for i in this: print(i)
#Exercise 5-------------------------------------------------------------------
def fun(n):
    for i in range(n,0,-1):
        yield i
n = int(input())
this = fun(n)
for i in this: print(i)

