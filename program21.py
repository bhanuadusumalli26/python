#python program to Find sum of Natural Numbers
limit=int(input("Enter the limit:"))
#initialize the sum
sum=0
for i in range(1,limit+1):
    sum+=i
print("Sum of natural numbers upto",limit,"is :",sum)