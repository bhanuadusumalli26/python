# Finding factorial by using recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = int(input("Enter a number: "))
# check if the number is negative
if num < 0:
    print("Sorry,factorial doesn't exist for negative Numbers")
elif num == 0:
    print("Factorial of Zero is 1")
else:
    print("The factorial of ", num, "is", recur_factorial(num))
