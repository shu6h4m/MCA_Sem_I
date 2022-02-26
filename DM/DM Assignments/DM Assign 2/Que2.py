'''
Q2) Write a program to find a Preorder, Inorder and Postorder Traversal of 3-ary Tree.
'''
import copy

def array3tree(nodes): #function to create 3 ary tree
    #dict will contain parents and child nodes
    tree=dict()     
    nodeCheck=True  

    #iterating nodes
    for i in nodes:
        compare=[nodes[0]] 
        count=1

        #iterating loop to check when outer loop break
        for n in nodes: 
            if len(tree)==0: break

            #iterating in tree
            for child in tree.values():

                #check if Node is in tree 
                if n in child:      
                    compare.append(n)
                    count+=1
            if compare==nodes: nodeCheck=False
            #if statement to add Node to tree with no child
            if n not in  tree: 
                tree[n]=[]
        if nodeCheck==False:break #to break loop when all Node placed in tree

        
        while(True): #loop to take number of child Node for root from user
            connection=int(input(f"\nEnter the number of child Node '{i}' have(atmost 3): "))
            if connection<=3 and connection<=(len(nodes)-count):
                break #break loop when child Node less than 3 and child also less than total Node remain which are not child Node yet
            print('Enter correct number of connection!!')
        #loop to take child nodes from user
        while(True):
            childNode=[ i for i in input(f"\nEnter the child Node of '{i}':\n").split()] #takingig child Node from user
            tree[i]=childNode   #add child Node to parent Node in tree
            if len(childNode)!=connection or (i in childNode): #to check user enter correct number of child Node
                print('Enter correct number of chile nodes or correct child Node!!')
                continue 
            flag=True   #to check when loop is break
            for child in childNode: #iterting in child
                for childs in tree.values():
                    #to check if child Node user enter is not child Node of another parent
                    if ((child in childs) and (childs!=tree[i])) or child not in nodes: 
                        print('Enter correct child nodes!!')
                        flag=False
                        break
                if flag==False: break
            if flag==True: break    #breal loop when child nodes are correct
    return tree

#function to traverse tree in post_order
def post_order(tree,root,result=''):
    if tree[root]==[]: #when Node not have any child Node
        return root     #return root
    else:
        for i in tree[root]:      #loop to visit left Node then right Node then root
            result=result+post_order(tree,i)+' --> '
        tree[root]=[]
        result=result+post_order(tree,root) #return the post_order traversed of tree
        return result


def pre_order(tree,root,result=''): #function to traverse tree in pre_order
    #when root not have child Node return root
    if tree[root]==[]: 
        return root     
    else:
        #visit root 
        result=result+ root 
        for i in tree[root]:
            result=result+' --> '+ pre_order(tree,i)
        #return all visited Node    
        return result   


def in_order(tree,root,result=''): #function to traverse tree in in in_order
    #when root not have child Node return root
    if tree[root]==[]:  
        return root
    else:
        #loop to visit
        for i in tree[root]:
            if result!='' and result[-1].isalnum(): result=result +' --> '
            result=result+in_order(tree,i)
            if tree[root].index(i)+1==1:
                result=result+' --> '+root
            #return all visited Node
        return result   

#driver code
nodes=[i for i in input('\nEnter the Nodes with space b/w each Node:\n').split()]

tree=array3tree(nodes) #calling function to create tree

print("\nParent Node\t\tChild Node(from left to right)") #printing tree
for parent,child in tree.items():
    print(parent,'\t\t:\t',*child,sep=' ')
tree1=copy.deepcopy(tree)

#callling function to traversed the tree
print("\nVisited Node if Postordered Traversal are \n",post_order(tree1,nodes[0]))
print("\nVisited Node if Preordered Traversal are \n",pre_order(tree,nodes[0]))
print("\nVisited Node if Inordered Traversal are \n",in_order(tree,nodes[0]))