'''
Q2 Program to impliment Tower of Hanoi (Iterative)
'''


#Function to show the movement of disks 
def moveDisk(fromPole,toPole,disk) :
    print("Move the disk ",disk," from ",fromPole," to ", toPole) 

#Function to implement legal movement between two poles 
def moveDisksBetweenTwoPoles(src_list,dest_list,s,d):

    ''' src_list = list containing disks on source pole
        dest_list = list containing disks on destination pole
        s = string named "Source"
        d = string named "Destination"
    '''
    
    #When src_list is empty 
    if (src_list == []) :
        disk = dest_list.pop()
        src_list.append(disk) 
        moveDisk(d, s, disk) 

    #When dest_list is empty
    elif (dest_list == []) :
        disk = src_list.pop()
        dest_list.append(disk) 
        moveDisk(s, d, disk)

    else :
        src_TopDisk = src_list.pop() 
        dest_TopDisk = dest_list.pop()
        
        #When top disk of src_list > top disk of dest_list 
        if (src_TopDisk > dest_TopDisk) :
            src_list.append(src_TopDisk) 
            src_list.append(dest_TopDisk) 
            moveDisk(d, s, dest_TopDisk); 

        #When top disk of src_list < top disk of dest_list 
        else:
            dest_list.append(dest_TopDisk) 
            dest_list.append(src_TopDisk) 
            moveDisk(s, d, src_TopDisk) 
  

def tower_of_hanoi_iterative(n,s,a,d):
    '''
        n = Number of disks
        s = Source Pole
        a = Auxiliary Pole
        d = Destination Pole
    '''
    total_moves = 2**n - 1

    src_list=[]
    aux_list=[]
    dest_list=[]

    '''
    In this program lists are used to implement stacks.
    Last element of list is considered as top of stack.
    We use pop() function to remove disk from list and
    append() function to insert disk at end of list.
        src_list = [4,3,2,1]
        Disk number 4 is largest and Disk number 1 is smallest.
        Disk 1 represents top of stack and disk 1 is top disk on the pole.
    '''
        
    #Larger disks will be pushed first
    for i in range(n,0,-1):
        src_list.append(i)
        
    #If number of disks is even, then interchange destination pole and auxiliary pole
    if(n%2==0):
        temp = d
        d = a
        a = temp

    for i in range(1,total_moves+1):
        if i%3 == 1:
            moveDisksBetweenTwoPoles(src_list, dest_list, s, d)
            
        elif i%3 == 2:
            moveDisksBetweenTwoPoles(src_list,aux_list, s, a)
            
        elif i%3 == 0:
            moveDisksBetweenTwoPoles(aux_list,dest_list, a, d)

# Defining main function
def main():
    n=int(input("Enter number of disks : "))#Input number of disks 
    tower_of_hanoi_iterative(n,"Source","Auxiliary","Destination")

# Calling main function
if __name__ == "__main__":
    main()
