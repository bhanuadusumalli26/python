#python program to Make a basic calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
    #take input from the user
    choice=input("Enter choice(1/2/3/4)")
    #check if choice is one of the four options
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second  number:"))
        except ValueError:
            print("Invalid input.Please enter a number")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,div(num1,num2))
        next_calculation=input("Let's do next calculation?(yes/no)")
        if next_calculation=="no":
            break
    else:
        print("Invalid Input")