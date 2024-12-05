#python program to calculate the Natural Logarithm of any number
import math
num=float(input("Enter a number:"))
if num <= 0:
    print("please enter a positive number")
else:
    #calculate the natural Logarithm(base e) of the number
    result=math.log(num)
    print(f"The natural Logarithm of {num} is:{result}")
