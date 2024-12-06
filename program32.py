#Function to  find the sum of elements in an array
def sum_of_array(arr):
    total=0
    for element in arr:
        total+=element
    return total
arr=[1,2,3,4,5]
result=sum_of_array(arr)
print(f"The sum of elements in an array:{result}")