""" 
9. Write a recursive python function to print octal of a given decimal number
 """
def fun(n):
    if n>1:
        fun(n//8)
    print(n%8,end="")
fun(int(input("Enter the decimal number:")))         

#========================================OUTPUT====================================
""" 
Enter the decimal number:89
131
 """