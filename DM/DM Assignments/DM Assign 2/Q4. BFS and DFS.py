class Graph:
    def __init__(self,nodes):
        self.nodes=nodes            #list conating all vertex
        self.adj_List=dict()        #dict/ adjacency list

        for vertex in nodes:    
            self.adj_List[vertex]=list()
    
    #adding edge to verties
    def addEdge(self,vertex,edges):
        #irritating in edges
        for edge in edges:
            #when eged is not present in vertex list
            if edge not in self.adj_List[vertex]:
                self.adj_List[vertex].append(edge)
            #when edge is not present vertex list
            if vertex not in self.adj_List[edge]:
                self.adj_List[edge].append(vertex)
        return self.adj_List    #return Adjacency list

    def printGraph(self):
        print('\nVertex\t:\tEdeges')
        for vertex,edge in self.adj_List.items():
            print(vertex,'\t:\t',edge)

#function for BFS graph traversal
def bfs(graph_dict,startVertex):
    queue=[startVertex]         #queue initally containg starting vertex
    visited=[startVertex]       #list containg vistied node
    BFS=''                      #will contains BFS result

    #loop until queue is not empty
    while len(queue)!=0:
        current=queue.pop(0)    #dequeue the queue
        BFS=BFS+'-->'+current   #add dequeue to BFS

        #irritating through neighbour vertex
        for adj_vertex in graph_dict[current]:
            #when vertex is not visted
            if adj_vertex not in visited:
                queue.append(adj_vertex)
                visited.append(adj_vertex) 

    if len(visited)==len(graph_dict):    return BFS #return BFS result
    else:
        print("Breadth first search(BFS) is not possible")
        exit()

#function to create DFS graph traversal
def dfs(graph_dict,startVertex):
    stack=[startVertex]         #stack initally containg starting vertex
    visited=[startVertex]       #lisit containg visited node
    #loop until stack not empty
    while len(stack)!=0:
        current=stack[-1]   #peek the stack

        for adj_vertex in graph_dict[current]:
            flag=True
            #if neighbour not visited
            if adj_vertex not in visited:   
                stack.append(adj_vertex)    #push vertex to stack
                visited.append(adj_vertex)  #add vertex to vistied list
                flag=False
                break
        
        if flag:
            stack.pop()                     #pop the element from stack
    
    if len(visited)==len(graph_dict):return visited  #return DFS result
    else:
        print("Depth First Search (DFS) is not possible")
        exit()

#driver code
def main():
    nodes=[i for i in input('\nEnter the All the vertex in graph with space between each vertex\n').split()]
        
    graph=Graph(nodes)
    print('\n*************************************************************************************************')

    #loop to add egeds
    for vertex in nodes:
        graph_dict=graph.addEdge(vertex,[edge for edge in input(f"\nEnter all Edge of '{vertex}' with space between each eadge:\n").split()])
    
    print('\n*************************************************************************************************')
    #printing graph adjacent list
    graph.printGraph()
    
    print('\n*************************************************************************************************')
    while(True):
        print('\nFor Breadth First Search Enter --> 1\nFor Depth First Search Enter --> 2\nFor Exit Enter -->3')
        option=input("Enter the option from above: ")
    
        print('\n*************************************************************************************************')
    
        if option=='3': break

        while True:
            startVertex=input('\nEnter the starting Node: ') #taking starting vertex from user
            if startVertex in nodes:                           #checking if entered staring vertex is in graph
                break
            print("Enter the correct starting Vertex")
        
        if option=='1': #for BFS
            print('\nBreadth First Search (BFS) \n',bfs(graph_dict,startVertex))
        elif option=='2': #for DFS
            dfsResult=dfs(graph_dict,startVertex)
            print('\nDepth First Search (DFS) \n',*dfsResult,sep=' --> ')
        else:
            print('Enter the wrong option!! try again')
        
        print('\n*************************************************************************************************')

if __name__=="__main__":
    main()