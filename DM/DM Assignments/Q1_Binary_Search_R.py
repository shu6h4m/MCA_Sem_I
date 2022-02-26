'''
Q1. Program to implement Binary Search(Recursive).
''' 
  
def binarySearch (arr, l, r, x): # Returns index of x in arr if present, else -1 
  
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
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