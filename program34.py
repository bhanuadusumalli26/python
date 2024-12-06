#Python program for Array rotation
def rorate_array(arr,d):
    n=len(arr)
    if d<0 or d>=n:
        return "Invalid rotation value"
    #Create a new array to store the rotated elements
    rotated_array=[0]*n
    #Perform the rotation
    for i in range(n):
        rotated_array[i]=arr[(i+d)%n]
    return rotated_array
#Input Array
arr=[1,2,3,4,5]
d=2
result=rorate_array(arr,d)
print(f"Original array:{arr}")
print(f"Rotated Array:{result}")