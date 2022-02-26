#circular queue class having constructor,enqueue and dequeue methods
class circularQueue:
    # constructor for intilaising queue
    def __init__(self,size):
        self.front=-1
        self.rear=-1
        self.size=size
        self.queue=list(range(size))
    #method for inserting record in queue
    def enqueue(self,record):
        #checking whether queue is full or not
        if (self.rear+1)%self.size==self.front:
            print("queue is full")
        elif self.front==-1:
            self.front=0
            self.rear=(self.rear+1)%self.size
        # adding record to queue
            self.queue[self.rear]=record
        else:
             self.rear=(self.rear+1)%self.size
             self.queue[self.rear]=record    
    #method for taking out record from queue
    def dequeue(self):
        #checking if queue is empty or not
        if self.front==-1:
            return 0
        elif self.front==self.rear and self.front!=-1:
            record=self.queue[self.front]
            self.front=self.rear=-1
            #print("dequeued element is: ",record)
            return record
        else:
            record=self.queue[self.front]
            self.front=(self.front+1)%self.size
            #print("dequeued element is: ",record)
            return record
    #method for displaying records in queue
    def display(self):
        s=''
        if self.front==-1:
            print("Nothing in queue")
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
        r=int(input("enter no. to be enqueue"))
        obj.enqueue(r)
    elif ch=='2':
        if obj.front==-1:
            print("empty queue")
        else:
            print("dequeued element is",obj.dequeue())
    elif ch=='3':
        print(obj.display())
    else:
        print("wrong choice")                    
              
# user input for size of circular queue        
n=int(input("enter size of circular queue: "))
obj=circularQueue(n)
flag='y'
while flag=='y':
    print("press 1 for enqueue")
    print("press 2 for dequeue")
    print("press 3 for display")
    ch=input("enter your choice: ")
    choice(ch)
    flag=input("do you want to continue?(y/n)")