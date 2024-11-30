#method1
#swapping values of two variables without using third variable
a=eval(input("enter the first number:"))
b=eval(input("enter the second  number:"))
print(f"original values: a={a}, b={b}")
a=a+b
b=a-b
a=a-b
print(f"swapped values: a={a},b={b}")
#method2
#swapping variables by using assignment
a=eval(input("enter the first number"))
b=eval(input("enter the second  number"))
print(f"original values: a={a}, b={b}")
a,b=b,a
print(f"swapped values: a={a},b={b}")