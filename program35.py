#python program to split the Array and Add the first part to the End
def split_and_add(arr,k):
    if k<0 or k>=len(arr):
        return arr
    #Split the array into Two parts
    first_part=arr[:k]
    second_part=arr[k:]
    #Add the first part to the End of the Second part
    Result=second_part+first_part
    return Result
#Test the Function
arr=[1,2,3,4,5]
k=4
result=split_and_add(arr,k)
print(f"Original array:{arr}")
print(f"Rotated Array:{result}")