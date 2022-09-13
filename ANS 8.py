""" 
8. Write a recursive python function to print binary of a given decimal number.
 """
def fun(n):
    if n>1:
        fun(n//2)
    print(n%2,end="")
fun(int(input("Enter the integer:")))  

#=====================================OUTPUT=================================
""" 
Enter the integer:52
110100
 """