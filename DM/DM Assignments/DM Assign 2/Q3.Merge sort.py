#program for recurrence relation T(n)=2T(n/2)+1. i.e. Merge Sort

import math

#function to merge the two sub list
def merge(left_listNum,right_listNum,listNum):
    i=0
    j=0
    r=0

    #merging two sub list
    while i<len(left_listNum) and j<len(right_listNum):
        if left_listNum[i]<right_listNum[j]:
            listNum[r]=left_listNum[i]
            r=r+1
            i=i+1
        else:
            listNum[r]=right_listNum[j]
            r=r+1
            j=j+1
    
    while i <len(left_listNum):
        listNum[r]=left_listNum[i]
        i=i+1
        r=r+1
    
    while j<len(right_listNum):
        listNum[r]=right_listNum[j]
        j=j+1
        r=r+1

    return listNum


def mergeSort(listNum): #function for merge sort
    if len(listNum)>1:
        
        mid= len(listNum)//2 #find mid od list

        left_listNum=listNum[:mid]
        right_listNum=listNum[mid:] #dividing listNum into subList containg half element each

        mergeSort(left_listNum)
        mergeSort(right_listNum) #calling function to sort both halves

        merge(left_listNum,right_listNum,listNum)  #calling function to merge to halves

        
        return listNum #returning sorted listNum


def complexity(): #function to find complexity using master theorm
    print("\nComplexity For T(n)=2T(n/2)+1 i.e merge sort is")
    p=2
    q=2
    r=0
    s=0

    log=int( math.log(p,q) )

    #applying master thoerm

    if p>q**r:
        print(f"T(n)= O( n^{log} )" )
    elif p==q**r:
        if s>-1:
            print(f"T(n)= O( n^{log} * ( log(n) )^{s+1} ) ")
        elif s==-1:
            print(f"T(n)= O( n^{log} * log(log(n))) )")
        elif s<-1:
            print(f"T(n)= O( n^{log} ) ")
    elif p<q**r:
        if s>=0:
            print(f"T(n)= O( n^{r} * ( log(n) )^{s} )")
        elif s<0:
            print(f"T(n)= O( n^{r} ) ")

def main(): #driver code
    while True: #taking numbers form user
        try:
            listNum=[int(i) for i in input("Enter the numbers with space\n").split()]
            break
        except:
            print("Enter the Number!!")
    
    print(f"\nBefore Sort \n{listNum}")

    print("\nAfter Merge Sort:")
    
    print(mergeSort(listNum)) #calling function for merge sort

    complexity() #calling function to get complexity

if __name__=="__main__":
    main()