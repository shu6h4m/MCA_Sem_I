'''
Q1. Program to implement Binary Search (Iterative). 
'''


def binarySearch(arr, l, r, x): 
# It returns location of x in given array arr  
# if present, else returns -1  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1
  
# Driver Code 
arr = [] 
n=int(input("enter no. of elements in list :"))
for i in range(n):
    ele=input()
    arr.append(ele)
x=input("enter no. to be searched") 
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")