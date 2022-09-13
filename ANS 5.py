""" 
5. Write a recursive python function to calculate sum of cubes of first N natural numbers

 """
def fun(n):
    if n>1:
        n=n**3+fun(n-1)
      
    return n    
print(fun(int(input("Enter the value of n:"))))

#=================================OUTPUT========================================
""" 
Enter the value of n:5
225
 """ 