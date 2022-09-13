""" 
10. Write a recursive python function to find the Nth term of the Fibonacci series
 """
def fun(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)
x=int(input("How many treams you want to be print:"))               
for i in range(1,x+1):
    print(fun(i),end=" ")

#====================================OUTPUT=====================================
# How many treams you want to be print:8
# 0 1 1 2 3 5 8 13     