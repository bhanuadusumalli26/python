#python program to find HCF  of two input numbers
def compute_HCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print("The hcf of two numbers: ",compute_HCF(num1,num2),)
    