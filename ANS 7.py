""" 
7. Write a recursive python function to calculate sum of the digits of a given number

 """
def fun(n) :
    if n>1:
        n=(n%10)+fun(n//10)
    return n
print(fun(int(input("Enter the digit:")))) 

#==============================OUTOUT===========================================
""" 
Enter the digit:5678
26
 """
