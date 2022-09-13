""" 
1. Write a recursive python function to calculate sum of first N natural numbers

 """
s=0
def fun(n):
    if n>0:
        n=n+fun(n-1)
      
    return n    
print(fun(int(input("Enter the value of n:"))))

#=======================================OUTPUT===================================
""" 
Enter the value of n:10
55
 """