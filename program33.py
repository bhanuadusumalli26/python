#python program to find the largest element in the array
def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    #Initialiaze the first element as the largest element
    Largest_element=arr[0]
    for element in arr:
        if element>=Largest_element:
            Largest_element=element
    return Largest_element
#Example usage:
my_array=[99,101,103,105,109,104]
result=find_largest_element(my_array)
print(f"The largest element in the array:{result}")