class Graph:
    def __init__(self,nodes):
        self.nodes=nodes            #list conating all vertex
        self.adj_List=dict()        #dict/ adjacency list
        
        for vertex in nodes:    
            self.adj_List[vertex]=list()
    
    #adding edge to verties
    def addEdge(self,vertex,edges):
        #irritating in enges
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
    return visited

#Function to check if all no-zero degree vertex connected
def isConnected(graph_dict):
    zeroDegree=[]           #list will contain zero degree vertex
    for i in graph_dict:    #loop to findout zero degree vertex
        if len(graph_dict[i])==0:
            zeroDegree.append(i)

    # to get starting vertex for dfs search
    for vertex in graph_dict:
        if graph_dict[vertex]!=0:
            startVertex=vertex
            break
    visited=dfs(graph_dict,startVertex) #calling function for dfs
    if len(visited)+len(zeroDegree)==len(graph_dict):   #checking all non-zero degree vertex is connected or not
        return True
    else: return False
        
#function to check if graph have Eulerian circuit or not
def Eulerian(graph_dict):
    if isConnected(graph_dict)==False:
        return False
    odd=0       #count vertices with odd degree
    for vertex in graph_dict:
        if len(graph_dict[vertex])%2!=0:
            odd=odd+1
    
    if odd==0: return True
    else: return False

#driver code
def main():
    nodes=[i for i in input('Enter the All the vertex in graph with space between each vertex:\n ').split()]

    graph=Graph(nodes)
    
    for vertex in nodes:        #loop to add edegs

        #while loop to take edges from user then check if its correct edge
        while True:
            flag=True   #flag to decide when break while loop
            #taking edges for vertex from user
            edges=[edge for edge in input(f"\nEnter all Edge of '{vertex}' (eg: if vertex is A and edge is AB then type B):\n").split()]
            #loop to check if edge is vaild
            for edge in edges:
                if edge not in nodes:
                    print('Enter correct vertexs!!')
                    flag=False
                    break       #break when edge is not correct
            if flag: break      #break when edge is correct

        graph_dict=graph.addEdge(vertex,edges)

    graph.printGraph()  #printing graph adjacent list
    print("\nGraph has a Eulerian Circuit") if Eulerian(graph_dict) else print("Graph not have a Eulerian Circuit")

if __name__=="__main__":
    main()