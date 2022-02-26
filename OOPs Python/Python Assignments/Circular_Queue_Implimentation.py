'''
Assignment 21 Circular Queue Implimentation

Implement Queue class, having following functions:
1. Enqueue: to insert an element, before insertion untill queue is not full.
2. Dequeue: to delete an element, before deletion, untill queue should not be empty.
3. Display: to display elements of the list
Also, note that the size of queue is fix i.e. queue can have a limited number of elements.

Submitted by Subham Sharma
IDE Used https://www.onlinegdb.com/  :)
'''
class QueueCircular:
    
    def __init__(self,size):
        '''
        To intilaise the values of queue
        '''
        self.front=-1
        self.rear=-1
        self.size=size
        self.queue=list(range(size))
    
    def enqueue(self,element):
        '''
        To insert element in queue
        '''
        if (self.rear+1)%self.size==self.front: #checking whether queue is full or not
            print("Sorry!! \nQueue is Full")

        elif self.front==-1:
            self.front=0
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element # adding element to queue
        else:
             self.rear=(self.rear+1)%self.size
             self.queue[self.rear]=element    
    
    def dequeue(self):
        '''
        To take out element from the queue
        ''' 
        if self.front==-1: #checking if queue is empty or not
            return 0

        elif self.front==self.rear and self.front!=-1:
            element=self.queue[self.front]
            self.front=self.rear=-1
            return element
        else:
            element=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return element
    
    def display(self):
        '''
        To display elements in queue
        '''
        s=''
        if self.front==-1:
            print("Queue is Empty !!\nNothing to Show")
        elif self.front != -1:
            if self.front<=self.rear:
                for i in range(self.front,self.rear+1):
                    s=s+str(self.queue[i])+" "
            else:
                for i in range(self.front,self.size):
                    s=s+str(self.queue[i])+" "
                for i in range(0,self.rear+1):
                    s=s+str(self.queue[i])+" "
        return s

def choice(ch):
    if ch=='1':
        r=int(input("Enter Data to Enqueue :  "))
        o1.enqueue(r)
    elif ch=='2':
        if o1.front==-1:
            print("Nothing to Dequeue\nQueue Is Empty !!")
        else:   
            print(o1.dequeue()," Dequeued from Queue" )
    elif ch=='3':
        print(o1.display())
    else:
        print("Wrong Choice")                    
                    
n=int(input("\nEnter size of Circular Queue : "))

o1=QueueCircular(n) #creating object
untill='y'
while untill=='y':
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    print(" Press 1 for Enqueue")
    print(" Press 2 for Dequeue")
    print(" Press 3 for Display")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    ch=input("\nEnter Your Choice: ")
    choice(ch)
    untill=input("\nPress y if You Want To Continue : ")
    