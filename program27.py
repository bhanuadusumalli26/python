#python program to display the Fibonacci sequence Using Recursion
def recur_fibo(n):
    if n<=1:
        return n
    else:
         return recur_fibo(n-1)+recur_fibo(n-2)
nterms=int(input("Enter the number of terms:"))
if nterms<=0:
    print("Invalid Input")
else:
    print("Fibbonacci Sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
