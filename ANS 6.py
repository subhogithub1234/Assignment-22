""" 
6. Write a recursive python function to calculate the factorial of a number.

 """
def fun(n):
    if n>1:
        n=n*fun(n-1)
      
    return n    
print(fun(int(input("Enter the value of n:"))))

#====================================OUTPUT====================================
""" 
Enter the value of n:5
120
 """