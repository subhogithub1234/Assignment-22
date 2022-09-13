""" 
2. Write a recursive python function to calculate sum of first N even natural numbers

 """

def fun(n) :
    if n>0:
         pass
    return(n)     
    
x=int(input("Enter the value of N:"))
s=0
for i in range(1,(x*2)+1):
    if i%2==0:
        fun(i)
        s=s+i
print(s)

#======================================OUTPUT==================================
""" 
Enter the value of N:10
110
 """