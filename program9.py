#finding roots of a quadratic equation
import math
#Input coefficients
a=float(input("enter coefficient a:"))
b=float(input("enter coefficient b:"))
c=float(input("enter coefficient c:"))
#calculate the discriminant
discriminant=((b**2) -(4*a*c))
#check if the discriminant is positive, negative,or Zero
if discriminant > 0:
    #Two real and distinct roots
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print(f"root1:{root1}")
    print(f"root2:{root2}")
elif discriminant==0:
    root= -b/(2*a)
    print(f"root:{root}")
else:
    real_part= -b/(2*a)
    imaginary_part=math.sqrt(abs(discriminant))/(2*a)
    print(f"root1:{real_part} + {imaginary_part}i")
    print(f"root2:{real_part}+ {imaginary_part}i")