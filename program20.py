#Armstrong numbers in between the given interval
lower=int(input("Enter a number:"))
upper=int(input("Enter a number:"))
for num in range(lower,upper+1):
    #calclulate the length of a number
    num_str=str(num)
    num_digits=len(num_str)
    sum=0
    temp_num=num
    while num>0:
        digit=num%10
        sum+=digit**num_digits
        num=num//10
    if sum==temp_num:
        print(sum)
    
