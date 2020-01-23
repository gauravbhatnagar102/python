def gb(a,b):
    print(a+b)
def gb1(a,b):
    print(a-b)
def gb2(a,b):
    print(a*b)
def gb3(a,b):
    print(a/b)
def gb4(n):             #Recursion
    if n==1:            #Base Case
        return 1
    return n*gb4(n-1)   #Recursive Case
def gb5(n):             #Print N natural numbers in reverse order through Recursion
    if n==1:
        print(1)
    else:
        print(n)
        gb5(n-1)
