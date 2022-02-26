'''
Q2 Program to impliment Tower of Hanoi (Recursive)
'''

def tower_of_hanoi_recursive(n,s,a,d):
    '''
        n = Number of disks
        s = Source Pole
        a = Auxiliary Pole
        d = Destination Pole
    '''

    if(n==1):
        print("Move the disk ",n," from ",s," to ", d)

    else :
        tower_of_hanoi_recursive(n-1,s,d,a)
        print("Move the disk ",n," from ",s," to ", d)
        tower_of_hanoi_recursive(n-1,a,s,d)


# Defining main function
def main():
    n=int(input("Enter number of disks : "))#Input number of disks 
    tower_of_hanoi_recursive(n,"Source","Auxiliary","Destination")

# Calling main function
if __name__ == "__main__":
    main()
