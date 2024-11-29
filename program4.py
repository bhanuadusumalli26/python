#swapping values of two variables
a=eval(input("enter the first number:"))
b=eval(input("enter the second  number:"))
print(f"original values: a={a}, b={b}")
temp=a
a=b
b=temp
print(f"swapped values: a={a},b={b}")